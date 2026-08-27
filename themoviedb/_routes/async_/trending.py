from themoviedb import schemas
from themoviedb._endpoints.misc import (
    TRENDING_MOVIE_DAY,
    TRENDING_MOVIE_WEEK,
    TRENDING_PERSON_DAY,
    TRENDING_PERSON_WEEK,
    TRENDING_TV_DAY,
    TRENDING_TV_WEEK,
)
from themoviedb._routes.async_._base import Base


class Trending(Base):
    async def movie_daily(self, *, page: int = 1) -> schemas.Movies:
        return await self._request_endpoint(TRENDING_MOVIE_DAY, page=page)

    async def movie_weekly(self, *, page: int = 1) -> schemas.Movies:
        return await self._request_endpoint(TRENDING_MOVIE_WEEK, page=page)

    async def person_daily(self, *, page: int = 1) -> schemas.People:
        return await self._request_endpoint(TRENDING_PERSON_DAY, page=page)

    async def person_weekly(self, *, page: int = 1) -> schemas.People:
        return await self._request_endpoint(TRENDING_PERSON_WEEK, page=page)

    async def tv_daily(self, *, page: int = 1) -> schemas.TVs:
        return await self._request_endpoint(TRENDING_TV_DAY, page=page)

    async def tv_weekly(self, *, page: int = 1) -> schemas.TVs:
        return await self._request_endpoint(TRENDING_TV_WEEK, page=page)
