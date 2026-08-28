from typing import Any, Type
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from themoviedb import TMDb, aioTMDb
from themoviedb._core.config import ClientConfig
from themoviedb._core.request import build_request


def test_request_builder_normalizes_shared_parameters() -> None:
    config = ClientConfig(api_key="key", language="pt-BR", region="BR", timeout=5.0)

    request = build_request(
        config,
        "movie/1/images",
        params={"include_adult": False, "with_genres__in": "12,16", "ignored": None},
    )

    assert request.url == "https://api.themoviedb.org/3/movie/1/images"
    assert request.params == {
        "api_key": "key",
        "watch_region": "BR",
        "include_adult": "false",
        "with_genres.in": "12,16",
    }
    assert request.timeout == 5.0


def test_timeout_is_shared_with_sync_resources() -> None:
    session = MagicMock()
    response = session.request.return_value.__enter__.return_value
    response.json.return_value = {}
    client = TMDb(api_key="key", session=session, language="pt-BR", region="BR", timeout=3.5)

    client.movies().latest()

    session.request.assert_called_once_with(
        "GET",
        "https://api.themoviedb.org/3/movie/latest",
        params={"api_key": "key", "language": "pt-BR", "region": "BR", "watch_region": "BR"},
        timeout=3.5,
    )


@pytest.mark.parametrize("client_class", (TMDb, aioTMDb))
def test_client_resources_share_configuration_and_transport(client_class: Type[Any]) -> None:
    client = client_class(api_key="key", session=MagicMock())
    resource = client.movie(123)

    assert resource._config is client._config
    assert resource._transport is client._transport


@pytest.mark.asyncio
async def test_timeout_is_shared_with_async_resources() -> None:
    session = MagicMock()
    response = MagicMock()
    response.json = AsyncMock(return_value={})
    session.request.return_value.__aenter__ = AsyncMock(return_value=response)
    session.request.return_value.__aexit__ = AsyncMock(return_value=False)
    client = aioTMDb(api_key="key", session=session, language="pt-BR", region="BR", timeout=3.5)

    await client.movies().latest()

    session.request.assert_called_once_with(
        "GET",
        "https://api.themoviedb.org/3/movie/latest",
        params={"api_key": "key", "language": "pt-BR", "region": "BR", "watch_region": "BR"},
        timeout=3.5,
    )


def test_sync_client_context_reuses_and_closes_its_session() -> None:
    with patch("themoviedb._transports.sync.Session") as session_class:
        session = session_class.return_value
        response = session.request.return_value.__enter__.return_value
        response.json.return_value = {}

        with TMDb(api_key="key") as client:
            client.movies().latest()
            client.movies().popular()

    assert session_class.call_count == 1
    assert session.request.call_count == 2
    session.close.assert_called_once_with()


def test_sync_client_does_not_close_an_injected_session() -> None:
    session = MagicMock()

    with TMDb(api_key="key", session=session):
        pass

    session.close.assert_not_called()


@pytest.mark.asyncio
async def test_async_client_context_reuses_and_closes_its_session() -> None:
    with patch("themoviedb._transports.async_.ClientSession") as session_class:
        session = session_class.return_value
        response = MagicMock()
        response.json = AsyncMock(return_value={})
        session.request.return_value.__aenter__ = AsyncMock(return_value=response)
        session.request.return_value.__aexit__ = AsyncMock(return_value=False)
        session.close = AsyncMock()

        async with aioTMDb(api_key="key") as client:
            await client.movies().latest()
            await client.movies().popular()

    assert session_class.call_count == 1
    assert session.request.call_count == 2
    session.close.assert_awaited_once_with()


@pytest.mark.asyncio
async def test_async_client_does_not_close_an_injected_session() -> None:
    session = MagicMock()
    session.close = AsyncMock()

    async with aioTMDb(api_key="key", session=session):
        pass

    session.close.assert_not_awaited()
