# -*- coding: utf-8 -*-
from themoviedb import schemas, utils
from themoviedb.routes.base import Base


class Keyword(Base):
    def __init__(self, keyword_id: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.keyword_id = keyword_id

    async def details(self) -> schemas.Keyword:
        """Get a keyword details by id.

        See more: https://developers.themoviedb.org/3/keywords/get-keyword-details
        """
        data = await self.request(f"keyword/{self.keyword_id}")
        return utils.as_dataclass(schemas.Keyword, data)

    async def movies(self, *, page: int = 1, include_adult: bool = False) -> schemas.Movies:
        """Get the movies that belong to a keyword.

        See more: https://developers.themoviedb.org/3/keywords/get-movies-by-keyword
        """
        data = await self.request(f"keyword/{self.keyword_id}/movies", page=page, include_adult=include_adult)
        return utils.as_dataclass(schemas.Movies, data)
