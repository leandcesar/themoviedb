from typing import Any, Mapping, Optional


class TMDbError(Exception):
    """Base class for errors raised by this package."""


class TMDbTimeoutError(TMDbError):
    """A request exceeded the timeout configured for the client."""

    def __init__(self, method: str, url: str) -> None:
        self.method = method
        self.url = url
        super().__init__("{} {} timed out".format(method, url))


class TMDbResponseDecodeError(TMDbError):
    """A successful response could not be decoded as a TMDb JSON object."""

    def __init__(self, method: str, url: str, reason: str) -> None:
        self.method = method
        self.url = url
        self.reason = reason
        super().__init__("Could not decode response from {} {}: {}".format(method, url, reason))


class TMDbHTTPError(TMDbError):
    """TMDb responded with an unsuccessful HTTP status code."""

    def __init__(self, status_code: int, method: str, url: str) -> None:
        self.status_code = status_code
        self.method = method
        self.url = url
        super().__init__("{} {} returned HTTP {}".format(method, url, status_code))


class TMDbAuthenticationError(TMDbHTTPError):
    """TMDb rejected the supplied authentication credentials."""


class TMDbRateLimitError(TMDbHTTPError):
    """TMDb rejected the request because its rate limit was reached."""

    def __init__(self, status_code: int, method: str, url: str, retry_after: Optional[float] = None) -> None:
        self.retry_after = retry_after
        super().__init__(status_code, method, url)


def _http_error(
    status_code: int,
    method: str,
    url: str,
    headers: Optional[Mapping[str, Any]] = None,
) -> TMDbHTTPError:
    """Create the appropriate public error for an HTTP response."""
    if status_code in (401, 403):
        return TMDbAuthenticationError(status_code, method, url)
    if status_code == 429:
        return TMDbRateLimitError(status_code, method, url, _retry_after(headers))
    return TMDbHTTPError(status_code, method, url)


def _retry_after(headers: Optional[Mapping[str, Any]]) -> Optional[float]:
    if headers is None:
        return None
    value = headers.get("Retry-After")
    try:
        return float(value) if value is not None else None
    except (TypeError, ValueError):
        return None
