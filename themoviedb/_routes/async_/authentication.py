from themoviedb import schemas
from themoviedb._endpoints.authentication import (
    CREATE_GUEST_SESSION,
    CREATE_SESSION,
    CREATE_SESSION_WITH_LOGIN,
    CREATE_TOKEN,
    DELETE_SESSION,
)
from themoviedb._routes.async_._base import Base


class Authentication(Base):
    """Create and delete TMDb authentication sessions."""

    async def create_guest_session(self) -> schemas.GuestAuthentication:
        return await self._request_endpoint(CREATE_GUEST_SESSION)

    async def create_token(self) -> schemas.TokenAuthentication:
        return await self._request_endpoint(CREATE_TOKEN)

    async def create_session(self, request_token: str) -> schemas.Session:
        return await self._request_endpoint(CREATE_SESSION, json={"request_token": request_token})

    async def create_session_with_login(
        self, username: str, password: str, request_token: str
    ) -> schemas.TokenAuthentication:
        return await self._request_endpoint(
            CREATE_SESSION_WITH_LOGIN,
            json={"request_token": request_token, "username": username, "password": password},
        )

    async def delete_session(self, session_id: str) -> schemas.Response:
        return await self._request_endpoint(DELETE_SESSION, json={"session_id": session_id})
