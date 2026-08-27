from themoviedb import schemas
from themoviedb._endpoints.misc import CERTIFICATIONS_MOVIE, CERTIFICATIONS_TV
from themoviedb._routes.sync._base import Base


class Certifications(Base):
    def movie(self) -> schemas.Certifications:
        return self._request_endpoint(CERTIFICATIONS_MOVIE)

    def tv(self) -> schemas.Certifications:
        return self._request_endpoint(CERTIFICATIONS_TV)
