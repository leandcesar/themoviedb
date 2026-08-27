import asyncio
from inspect import isawaitable
from typing import Any, Dict, Mapping, Optional

from aiohttp import ClientResponseError, ClientSession, ContentTypeError

from themoviedb._core.request import Request
from themoviedb._core.response import normalize_response
from themoviedb.exceptions import TMDbResponseDecodeError, TMDbTimeoutError, _http_error


class AsyncTransport:
    """Send prepared requests without exposing ``aiohttp`` to route modules."""

    def __init__(self, session: Optional[ClientSession] = None) -> None:
        self._session = session
        self._owns_session = False

    @property
    def session(self) -> Optional[ClientSession]:
        return self._session

    async def open(self) -> None:
        """Start a reusable session owned by the client."""
        if self._session is None:
            self._session = ClientSession()
            self._owns_session = True

    async def close(self) -> None:
        """Close only a session created by this transport."""
        if self._owns_session and self._session is not None:
            await self._session.close()
            self._session = None
            self._owns_session = False

    async def send(self, request: Request) -> Dict[str, Any]:
        """Send a request, using an ephemeral session until ``open`` is called."""
        if self._session is not None:
            return await self._send_with_session(self._session, request)

        async with ClientSession() as session:
            return await self._send_with_session(session, request)

    @staticmethod
    async def _send_with_session(session: ClientSession, request: Request) -> Dict[str, Any]:
        request_kwargs: Dict[str, Any] = {"params": request.params}
        if request.json is not None:
            request_kwargs["json"] = request.json
        if request.timeout is not None:
            request_kwargs["timeout"] = request.timeout

        try:
            async with session.request(request.method, request.url, **request_kwargs) as response:
                try:
                    status_result: Any = getattr(response, "raise_for_status")()
                    if isawaitable(status_result):
                        await status_result
                except ClientResponseError as error:
                    raise _http_error(
                        response.status,
                        request.method,
                        request.url,
                        _headers(response.headers),
                    ) from error

                try:
                    data = await response.json()
                except (ContentTypeError, TypeError, ValueError) as error:
                    raise TMDbResponseDecodeError(request.method, request.url, str(error)) from error

                if not isinstance(data, Mapping):
                    raise TMDbResponseDecodeError(request.method, request.url, "expected a JSON object")
                return normalize_response(data)
        except asyncio.TimeoutError as error:
            raise TMDbTimeoutError(request.method, request.url) from error


def _headers(headers: Any) -> Optional[Mapping[str, Any]]:
    return headers if isinstance(headers, Mapping) else None
