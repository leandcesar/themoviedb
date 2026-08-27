from themoviedb import schemas
from themoviedb._endpoints.authentication import (
    CREATE_GUEST_SESSION,
    CREATE_SESSION,
    CREATE_SESSION_WITH_LOGIN,
    CREATE_TOKEN,
    DELETE_SESSION,
)
from themoviedb._routes.sync._base import Base


class Authentication(Base):
    """Create and delete TMDb authentication sessions."""

    def create_guest_session(self) -> schemas.GuestAuthentication:
        return self._request_endpoint(CREATE_GUEST_SESSION)

    def create_token(self) -> schemas.TokenAuthentication:
        return self._request_endpoint(CREATE_TOKEN)

    def create_session(self, request_token: str) -> schemas.Session:
        return self._request_endpoint(CREATE_SESSION, json={"request_token": request_token})

    def create_session_with_login(
        self, username: str, password: str, request_token: str
    ) -> schemas.TokenAuthentication:
        return self._request_endpoint(
            CREATE_SESSION_WITH_LOGIN,
            json={"request_token": request_token, "username": username, "password": password},
        )

    def delete_session(self, session_id: str) -> schemas.Response:
        return self._request_endpoint(DELETE_SESSION, json={"session_id": session_id})
