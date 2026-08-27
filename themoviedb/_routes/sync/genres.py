from themoviedb import schemas
from themoviedb._endpoints.misc import GENRES_MOVIE, GENRES_TV
from themoviedb._routes.sync._base import Base


class Genres(Base):
    def movie(self) -> schemas.Genres:
        return self._request_endpoint(GENRES_MOVIE)

    def tv(self) -> schemas.Genres:
        return self._request_endpoint(GENRES_TV)
