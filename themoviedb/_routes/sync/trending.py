from themoviedb import schemas
from themoviedb._endpoints.misc import (
    TRENDING_MOVIE_DAY,
    TRENDING_MOVIE_WEEK,
    TRENDING_PERSON_DAY,
    TRENDING_PERSON_WEEK,
    TRENDING_TV_DAY,
    TRENDING_TV_WEEK,
)
from themoviedb._routes.sync._base import Base


class Trending(Base):
    def movie_daily(self, *, page: int = 1) -> schemas.Movies:
        return self._request_endpoint(TRENDING_MOVIE_DAY, page=page)

    def movie_weekly(self, *, page: int = 1) -> schemas.Movies:
        return self._request_endpoint(TRENDING_MOVIE_WEEK, page=page)

    def person_daily(self, *, page: int = 1) -> schemas.People:
        return self._request_endpoint(TRENDING_PERSON_DAY, page=page)

    def person_weekly(self, *, page: int = 1) -> schemas.People:
        return self._request_endpoint(TRENDING_PERSON_WEEK, page=page)

    def tv_daily(self, *, page: int = 1) -> schemas.TVs:
        return self._request_endpoint(TRENDING_TV_DAY, page=page)

    def tv_weekly(self, *, page: int = 1) -> schemas.TVs:
        return self._request_endpoint(TRENDING_TV_WEEK, page=page)
