from dataclasses import dataclass
from typing import Any, Dict, Mapping, Optional

from themoviedb._core.config import ClientConfig


@dataclass(frozen=True)
class Request:
    """A fully prepared request for the TMDb API."""

    method: str
    url: str
    params: Dict[str, Any]
    json: Optional[Mapping[str, Any]] = None
    timeout: Optional[float] = None


def build_request(
    config: ClientConfig,
    path: str,
    *,
    method: str = "GET",
    json: Optional[Mapping[str, Any]] = None,
    params: Mapping[str, Any],
) -> Request:
    """Normalize route parameters and create an immutable request description."""
    query_params = {
        key.replace("__", "."): _serialize_query_value(value) for key, value in params.items() if value is not None
    }
    query_params = {**config.default_params, **query_params}

    if path.endswith("/images"):
        query_params.pop("region")
        query_params.pop("language")

    return Request(
        method=method,
        url="{}/{}/{}".format(config.host, config.version, path),
        params=query_params,
        json=json,
        timeout=config.timeout,
    )


def _serialize_query_value(value: Any) -> Any:
    """Serialize values with TMDb's documented boolean representation."""
    if value is True:
        return "true"
    if value is False:
        return "false"
    return value
