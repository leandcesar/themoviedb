from themoviedb import schemas
from themoviedb._endpoints._endpoint import Endpoint

CREATE_GUEST_SESSION = Endpoint("authentication/guest_session/new", schemas.GuestAuthentication)
CREATE_TOKEN = Endpoint("authentication/token/new", schemas.TokenAuthentication)
CREATE_SESSION = Endpoint("authentication/session/new", schemas.Session, method="POST")
CREATE_SESSION_WITH_LOGIN = Endpoint(
    "authentication/token/validate_with_login", schemas.TokenAuthentication, method="POST"
)
DELETE_SESSION = Endpoint("authentication/session", schemas.Response, method="DELETE")
