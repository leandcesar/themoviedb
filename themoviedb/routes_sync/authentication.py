from themoviedb import schemas, utils
from themoviedb.routes_sync._base import Base


class Authentication(Base):

    def create_guest_session(self) -> schemas.GuestAuthentication:
        """This method will let you create a new guest session.
        Guest sessions are a type of session that will let a user rate movies
        and TV shows but not require them to have a TMDB user account.

        See more: https://developers.themoviedb.org/3/authentication/create-guest-session
        """
        data = self.request("authentication/guest_session/new")
        return utils.as_dataclass(schemas.GuestAuthentication, data)

    def create_token(self) -> schemas.TokenAuthentication:
        """Create a temporary request token that can be used to validate a TMDB user login.

        See more: https://developers.themoviedb.org/3/authentication/create-request-token
        """
        data = self.request("authentication/token/new")
        return utils.as_dataclass(schemas.TokenAuthentication, data)
    
    def create_session(self, request_token: str) -> schemas.Session:
        """You can use this method to create a fully valid session ID once a user has
        validated the request token.

        See more: https://developers.themoviedb.org/3/authentication/create-session
        """
        data = self.request(
            "authentication/session/new",
            method="POST",
            json={"request_token": request_token},
        )
        return utils.as_dataclass(schemas.Session, data)
    
    def create_session_with_login(self, username: str, password: str, request_token: str) -> schemas.Session:
        """This method allows an application to validate a request token by entering
        a username and password.

        See more: https://developers.themoviedb.org/3/authentication/validate-request-token
        """
        data = self.request(
            "authentication/token/validate_with_login",
            method="POST",
            json={"request_token": request_token, "username": username, "password": password},
        )
        return utils.as_dataclass(schemas.TokenAuthentication, data)
    
    def delete_session(self, session_id: str) -> schemas.Response:
        """If you would like to delete (or "logout") from a session,
        call this method with a valid session ID.

        See more: https://developers.themoviedb.org/3/authentication/delete-session
        """
        data = self.request(
            "authentication/session",
            method="DELETE",
            json={"session_id": session_id},
        )
        return utils.as_dataclass(schemas.Response, data)
