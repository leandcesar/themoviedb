from typing import Any, Dict, Mapping, Optional, TypeVar

from requests import Session

from themoviedb._core.base import BaseRoute
from themoviedb._core.config import ClientConfig
from themoviedb._endpoints._endpoint import Endpoint
from themoviedb._transports.sync import SyncTransport
from themoviedb.utils import as_dataclass

T = TypeVar("T")
TBase = TypeVar("TBase", bound="Base")


class Base(BaseRoute):
    """Base class for synchronous TMDb resources."""

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        session: Optional[Session] = None,
        language: Optional[str] = None,
        region: Optional[str] = None,
        timeout: Optional[float] = None,
        _config: Optional[ClientConfig] = None,
        _transport: Optional[SyncTransport] = None,
    ) -> None:
        super().__init__(api_key=api_key, language=language, region=region, timeout=timeout, _config=_config)
        self._transport = _transport or SyncTransport(session)

    @property
    def session(self) -> Optional[Session]:
        return self._transport.session

    @session.setter
    def session(self, session: Session) -> None:
        self._transport.close()
        self._transport = SyncTransport(session)

    def request(self, path: str, method: str = "GET", **kwargs: Any) -> Dict[str, Any]:
        """Execute a route request through the synchronous transport."""
        json = kwargs.pop("json", None)
        request = self._build_request(path, method=method, json=json, params=kwargs)
        return self._transport.send(request)

    def _request_endpoint(
        self,
        endpoint: Endpoint[T],
        *,
        path_params: Optional[Mapping[str, object]] = None,
        **params: Any,
    ) -> T:
        """Execute an endpoint definition and deserialize its response."""
        path = endpoint.path(**(path_params or {}))
        data = self.request(path, method=endpoint.method, **params)
        return as_dataclass(endpoint.response_type, data)

    def close(self) -> None:
        """Close a reusable session owned by this client."""
        self._transport.close()

    def __enter__(self: TBase) -> TBase:
        self._transport.open()
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        self.close()
