# -*- coding: utf-8 -*-
from themoviedb import schemas, utils
from themoviedb.routes_sync._base import Base


class Genres(Base):
    def movie(self) -> schemas.Genres:
        """Get the list of official genres for movies.

        See more: https://developers.themoviedb.org/3/genres/get-movie-list
        """
        data = self.request("genre/movie/list")
        return utils.as_dataclass(schemas.Genres, data)

    def tv(self) -> schemas.Genres:
        """Get the list of official genres for TV shows.

        See more: https://developers.themoviedb.org/3/genres/get-tv-list
        """
        data = self.request("genre/tv/list")
        return utils.as_dataclass(schemas.Genres, data)
