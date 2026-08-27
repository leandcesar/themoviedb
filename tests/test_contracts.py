import importlib
import inspect
import pkgutil
from asyncio import TimeoutError
from typing import Any, Dict, Iterable, Tuple, Type
from unittest.mock import AsyncMock, MagicMock

import pytest
from aiohttp import ClientResponseError
from requests.exceptions import HTTPError, Timeout

from themoviedb import AsyncTMDbClient, TMDbClient
from themoviedb._core.request import Request
from themoviedb._routes.async_ import __path__ as ASYNC_ROUTES_PATH
from themoviedb._routes.sync import __path__ as SYNC_ROUTES_PATH
from themoviedb._transports.async_ import AsyncTransport
from themoviedb._transports.sync import SyncTransport
from themoviedb.exceptions import (
    TMDbAuthenticationError,
    TMDbRateLimitError,
    TMDbResponseDecodeError,
    TMDbTimeoutError,
)


def _public_methods(cls: Type[Any]) -> Dict[str, Any]:
    return {
        name: method
        for name, method in cls.__dict__.items()
        if inspect.isfunction(method) and not name.startswith("_")
    }


def _signature(method: Any) -> Tuple[Tuple[Any, ...], ...]:
    return tuple(
        (parameter.name, parameter.kind, parameter.default, parameter.annotation)
        for parameter in inspect.signature(method).parameters.values()
    )


def _route_modules(path: Iterable[str], package: str) -> Iterable[Any]:
    for module_info in pkgutil.iter_modules(path):
        if module_info.name != "_base":
            yield importlib.import_module("{}.{}".format(package, module_info.name))


def test_client_factory_contract_is_identical_for_sync_and_async() -> None:
    sync_methods = _public_methods(TMDbClient)
    async_methods = _public_methods(AsyncTMDbClient)

    assert set(sync_methods) == set(async_methods)
    for name, sync_method in sync_methods.items():
        assert _signature(sync_method) == _signature(async_methods[name])
        assert not inspect.iscoroutinefunction(sync_method)
        assert not inspect.iscoroutinefunction(async_methods[name])


def test_resource_contract_is_identical_for_sync_and_async() -> None:
    sync_modules = {
        module.__name__.rsplit(".", 1)[-1]: module
        for module in _route_modules(SYNC_ROUTES_PATH, "themoviedb._routes.sync")
    }
    async_modules = {
        module.__name__.rsplit(".", 1)[-1]: module
        for module in _route_modules(ASYNC_ROUTES_PATH, "themoviedb._routes.async_")
    }

    assert set(sync_modules) == set(async_modules)
    for module_name, sync_module in sync_modules.items():
        async_module = async_modules[module_name]
        sync_classes = {
            name: cls
            for name, cls in inspect.getmembers(sync_module, inspect.isclass)
            if cls.__module__ == sync_module.__name__
        }
        async_classes = {
            name: cls
            for name, cls in inspect.getmembers(async_module, inspect.isclass)
            if cls.__module__ == async_module.__name__
        }

        assert set(sync_classes) == set(async_classes), module_name
        for class_name, sync_class in sync_classes.items():
            async_class = async_classes[class_name]
            sync_methods = _public_methods(sync_class)
            async_methods = _public_methods(async_class)

            assert set(sync_methods) == set(async_methods), "{}.{}".format(module_name, class_name)
            for method_name, sync_method in sync_methods.items():
                async_method = async_methods[method_name]
                assert _signature(sync_method) == _signature(async_method)
                assert not inspect.iscoroutinefunction(sync_method)
                assert inspect.iscoroutinefunction(async_method)


def test_sync_transport_forwards_request_and_normalizes_response() -> None:
    session = MagicMock()
    response = session.request.return_value.__enter__.return_value
    response.json.return_value = {"watch/providers": {"BR": {}}}
    request = Request(
        method="POST",
        url="https://api.themoviedb.org/3/movie/1",
        params={"api_key": "key"},
        json={"request_token": "token"},
    )

    result = SyncTransport(session).send(request)

    session.request.assert_called_once_with("POST", request.url, params=request.params, json=request.json)
    response.raise_for_status.assert_called_once_with()
    assert result == {"watch_providers": {"BR": {}}}


def test_sync_transport_propagates_http_errors() -> None:
    session = MagicMock()
    response = session.request.return_value.__enter__.return_value
    response.raise_for_status.side_effect = RuntimeError("request failed")

    with pytest.raises(RuntimeError, match="request failed"):
        SyncTransport(session).send(Request("GET", "https://example.com", {}))

    response.json.assert_not_called()


def test_sync_transport_normalizes_rate_limit_errors() -> None:
    session = MagicMock()
    response = session.request.return_value.__enter__.return_value
    response.status_code = 429
    response.headers = {"Retry-After": "4"}
    response.raise_for_status.side_effect = HTTPError("too many requests")

    with pytest.raises(TMDbRateLimitError) as error:
        SyncTransport(session).send(Request("GET", "https://example.com", {}))

    assert error.value.status_code == 429
    assert error.value.retry_after == 4.0
    assert isinstance(error.value.__cause__, HTTPError)


def test_sync_transport_normalizes_timeout_and_decode_errors() -> None:
    timeout_session = MagicMock()
    timeout_session.request.side_effect = Timeout("timed out")

    with pytest.raises(TMDbTimeoutError) as timeout_error:
        SyncTransport(timeout_session).send(Request("GET", "https://example.com", {}))

    assert isinstance(timeout_error.value.__cause__, Timeout)

    decode_session = MagicMock()
    decode_response = decode_session.request.return_value.__enter__.return_value
    decode_response.json.return_value = ["unexpected"]

    with pytest.raises(TMDbResponseDecodeError, match="expected a JSON object"):
        SyncTransport(decode_session).send(Request("GET", "https://example.com", {}))


@pytest.mark.asyncio
async def test_async_transport_forwards_request_and_normalizes_response() -> None:
    session = MagicMock()
    response = MagicMock()
    response.json = AsyncMock(return_value={"watch/providers": {"BR": {}}})
    session.request.return_value.__aenter__ = AsyncMock(return_value=response)
    session.request.return_value.__aexit__ = AsyncMock(return_value=False)
    request = Request(
        method="POST",
        url="https://api.themoviedb.org/3/movie/1",
        params={"api_key": "key"},
        json={"request_token": "token"},
    )

    result = await AsyncTransport(session).send(request)

    session.request.assert_called_once_with("POST", request.url, params=request.params, json=request.json)
    response.raise_for_status.assert_called_once_with()
    assert result == {"watch_providers": {"BR": {}}}


@pytest.mark.asyncio
async def test_async_transport_propagates_http_errors() -> None:
    session = MagicMock()
    response = MagicMock()
    response.raise_for_status.side_effect = RuntimeError("request failed")
    response.json = AsyncMock()
    session.request.return_value.__aenter__ = AsyncMock(return_value=response)
    session.request.return_value.__aexit__ = AsyncMock(return_value=False)

    with pytest.raises(RuntimeError, match="request failed"):
        await AsyncTransport(session).send(Request("GET", "https://example.com", {}))

    response.json.assert_not_awaited()


@pytest.mark.asyncio
async def test_async_transport_normalizes_authentication_errors() -> None:
    session = MagicMock()
    response = MagicMock()
    response.status = 401
    response.headers = {}
    response.raise_for_status.side_effect = ClientResponseError(MagicMock(), (), status=401)
    session.request.return_value.__aenter__ = AsyncMock(return_value=response)
    session.request.return_value.__aexit__ = AsyncMock(return_value=False)

    with pytest.raises(TMDbAuthenticationError) as error:
        await AsyncTransport(session).send(Request("GET", "https://example.com", {}))

    assert error.value.status_code == 401
    assert isinstance(error.value.__cause__, ClientResponseError)


@pytest.mark.asyncio
async def test_async_transport_normalizes_timeout_and_decode_errors() -> None:
    timeout_session = MagicMock()
    timeout_session.request.return_value.__aenter__ = AsyncMock(side_effect=TimeoutError())

    with pytest.raises(TMDbTimeoutError) as timeout_error:
        await AsyncTransport(timeout_session).send(Request("GET", "https://example.com", {}))

    assert isinstance(timeout_error.value.__cause__, TimeoutError)

    decode_session = MagicMock()
    decode_response = MagicMock()
    decode_response.json = AsyncMock(return_value=["unexpected"])
    decode_session.request.return_value.__aenter__ = AsyncMock(return_value=decode_response)
    decode_session.request.return_value.__aexit__ = AsyncMock(return_value=False)

    with pytest.raises(TMDbResponseDecodeError, match="expected a JSON object"):
        await AsyncTransport(decode_session).send(Request("GET", "https://example.com", {}))
