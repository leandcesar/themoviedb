from typing import Any, Dict, Mapping, Optional

from themoviedb._core.config import ClientConfig
from themoviedb._core.request import Request, build_request


class BaseRoute:
    """Common state for a client facade and its resource objects."""

    TMDB_URL = "https://api.themoviedb.org"
    TMDB_VERSION = "3"

    def __init__(
        self,
        *,
        key: Optional[str] = None,
        language: Optional[str] = None,
        region: Optional[str] = None,
        timeout: Optional[float] = None,
        _config: Optional[ClientConfig] = None,
    ) -> None:
        self._config = _config or ClientConfig.from_values(
            key=key, language=language, region=region, timeout=timeout
        )

    @property
    def key(self) -> Optional[str]:
        return self._config.key

    @key.setter
    def key(self, key: str) -> None:
        self._config.key = key

    @property
    def language(self) -> str:
        return self._config.language

    @language.setter
    def language(self, language: str) -> None:
        self._config.language = language

    @property
    def region(self) -> str:
        return self._config.region

    @region.setter
    def region(self, region: str) -> None:
        self._config.region = region

    @property
    def timeout(self) -> Optional[float]:
        """Maximum time in seconds for each HTTP request, or ``None`` for the transport default."""
        return self._config.timeout

    @timeout.setter
    def timeout(self, timeout: Optional[float]) -> None:
        self._config.timeout = timeout

    @property
    def _host(self) -> str:
        return self._config.host

    @property
    def _version(self) -> str:
        return self._config.version

    @property
    def _params(self) -> Dict[str, Any]:
        return self._config.default_params

    def _build_request(
        self,
        path: str,
        *,
        method: str = "GET",
        json: Optional[Mapping[str, Any]] = None,
        params: Mapping[str, Any],
    ) -> Request:
        return build_request(self._config, path, method=method, json=json, params=params)
