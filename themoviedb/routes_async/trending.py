# -*- coding: utf-8 -*-
from themoviedb import schemas, utils
from themoviedb.routes_async._base import Base


class Trending(Base):
    async def movie_daily(self, *, page: int = 1) -> schemas.Movies:
        """Get the daily trending movies.

        See more: https://developers.themoviedb.org/3/trending/get-trending
        """
        data = await self.request("trending/movie/day", page=page)
        return utils.as_dataclass(schemas.Movies, data)

    async def movie_weekly(self, *, page: int = 1) -> schemas.Movies:
        """Get the weekly trending movies.

        See more: https://developers.themoviedb.org/3/trending/get-trending
        """
        data = await self.request("trending/movie/week", page=page)
        return utils.as_dataclass(schemas.Movies, data)

    async def person_daily(self, *, page: int = 1) -> schemas.People:
        """Get the daily trending people.

        See more: https://developers.themoviedb.org/3/trending/get-trending
        """
        data = await self.request("trending/person/day", page=page)
        return utils.as_dataclass(schemas.People, data)

    async def person_weekly(self, *, page: int = 1) -> schemas.People:
        """Get the weekly trending people.

        See more: https://developers.themoviedb.org/3/trending/get-trending
        """
        data = await self.request("trending/person/week", page=page)
        return utils.as_dataclass(schemas.People, data)

    async def tv_daily(self, *, page: int = 1) -> schemas.TVs:
        """Get the daily trending TV shows.

        See more: https://developers.themoviedb.org/3/trending/get-trending
        """
        data = await self.request("trending/tv/day", page=page)
        return utils.as_dataclass(schemas.TVs, data)

    async def tv_weekly(self, *, page: int = 1) -> schemas.TVs:
        """Get the weekly trending TV shows.

        See more: https://developers.themoviedb.org/3/trending/get-trending
        """
        data = await self.request("trending/tv/week", page=page)
        return utils.as_dataclass(schemas.TVs, data)
