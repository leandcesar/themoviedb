from typing import Any, Dict, Mapping, Optional

from requests import Session
from requests.exceptions import HTTPError, Timeout

from themoviedb._core.request import Request
from themoviedb._core.response import normalize_response
from themoviedb.exceptions import TMDbResponseDecodeError, TMDbTimeoutError, _http_error


class SyncTransport:
    """Send prepared requests without exposing ``requests`` to route modules."""

    def __init__(self, session: Optional[Session] = None) -> None:
        self._session = session
        self._owns_session = False

    @property
    def session(self) -> Optional[Session]:
        return self._session

    def open(self) -> None:
        """Start a reusable session owned by the client."""
        if self._session is None:
            self._session = Session()
            self._owns_session = True

    def close(self) -> None:
        """Close only a session created by this transport."""
        if self._owns_session and self._session is not None:
            self._session.close()
            self._session = None
            self._owns_session = False

    def send(self, request: Request) -> Dict[str, Any]:
        """Send a request, using an ephemeral session until ``open`` is called."""
        if self._session is not None:
            return self._send_with_session(self._session, request)

        with Session() as session:
            return self._send_with_session(session, request)

    @staticmethod
    def _send_with_session(session: Session, request: Request) -> Dict[str, Any]:
        request_kwargs: Dict[str, Any] = {"params": request.params}
        if request.json is not None:
            request_kwargs["json"] = request.json
        if request.timeout is not None:
            request_kwargs["timeout"] = request.timeout

        try:
            with session.request(request.method, request.url, **request_kwargs) as response:
                try:
                    response.raise_for_status()
                except HTTPError as error:
                    raise _http_error(
                        response.status_code,
                        request.method,
                        request.url,
                        _headers(response.headers),
                    ) from error

                try:
                    data = response.json()
                except (TypeError, ValueError) as error:
                    raise TMDbResponseDecodeError(request.method, request.url, str(error)) from error

                if not isinstance(data, Mapping):
                    raise TMDbResponseDecodeError(request.method, request.url, "expected a JSON object")
                return normalize_response(data)
        except Timeout as error:
            raise TMDbTimeoutError(request.method, request.url) from error


def _headers(headers: Any) -> Optional[Mapping[str, Any]]:
    return headers if isinstance(headers, Mapping) else None
