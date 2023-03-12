from themoviedb import schemas, utils
from themoviedb.routes.base import Base


class Genres(Base):

    async def movie(self) -> schemas.Genres:
        """Get the list of official genres for movies.

        See more: https://developers.themoviedb.org/3/genres/get-movie-list
        """
        data = await self.request("genre/movie/list")
        return utils.as_dataclass(schemas.Genres, data)

    async def tv(self) -> schemas.Genres:
        """Get the list of official genres for TV shows.

        See more: https://developers.themoviedb.org/3/genres/get-tv-list
        """
        data = await self.request("genre/tv/list")
        return utils.as_dataclass(schemas.Genres, data)
