from themoviedb import schemas
from themoviedb._endpoints.misc import GENRES_MOVIE, GENRES_TV
from themoviedb._routes.async_._base import Base


class Genres(Base):
    async def movie(self) -> schemas.Genres:
        return await self._request_endpoint(GENRES_MOVIE)

    async def tv(self) -> schemas.Genres:
        return await self._request_endpoint(GENRES_TV)
