from typing import Any, Dict, Mapping, Optional, TypeVar

from aiohttp import ClientSession

from themoviedb._core.base import BaseRoute
from themoviedb._core.config import ClientConfig
from themoviedb._endpoints._endpoint import Endpoint
from themoviedb._transports.async_ import AsyncTransport
from themoviedb.utils import as_dataclass

T = TypeVar("T")
TBase = TypeVar("TBase", bound="Base")


class Base(BaseRoute):
    """Base class for asynchronous TMDb resources."""

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        session: Optional[ClientSession] = None,
        language: Optional[str] = None,
        region: Optional[str] = None,
        timeout: Optional[float] = None,
        _config: Optional[ClientConfig] = None,
        _transport: Optional[AsyncTransport] = None,
    ) -> None:
        super().__init__(api_key=api_key, language=language, region=region, timeout=timeout, _config=_config)
        self._transport = _transport or AsyncTransport(session)

    @property
    def session(self) -> Optional[ClientSession]:
        return self._transport.session

    @session.setter
    def session(self, session: ClientSession) -> None:
        self._transport = AsyncTransport(session)

    async def request(self, path: str, method: str = "GET", **kwargs: Any) -> Dict[str, Any]:
        """Execute a route request through the asynchronous transport."""
        json = kwargs.pop("json", None)
        request = self._build_request(path, method=method, json=json, params=kwargs)
        return await self._transport.send(request)

    async def _request_endpoint(
        self,
        endpoint: Endpoint[T],
        *,
        path_params: Optional[Mapping[str, object]] = None,
        **params: Any,
    ) -> T:
        """Execute an endpoint definition and deserialize its response."""
        path = endpoint.path(**(path_params or {}))
        data = await self.request(path, method=endpoint.method, **params)
        return as_dataclass(endpoint.response_type, data)

    async def aclose(self) -> None:
        """Close a reusable session owned by this client."""
        await self._transport.close()

    async def __aenter__(self: TBase) -> TBase:
        await self._transport.open()
        return self

    async def __aexit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        await self.aclose()
