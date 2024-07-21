# -*- coding: utf-8 -*-
from themoviedb import schemas, utils
from themoviedb.routes_sync._base import Base


class Keyword(Base):
    def __init__(self, keyword_id: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.keyword_id = keyword_id

    def details(self) -> schemas.Keyword:
        """Get a keyword details by id.

        See more: https://developers.themoviedb.org/3/keywords/get-keyword-details
        """
        data = self.request(f"keyword/{self.keyword_id}")
        return utils.as_dataclass(schemas.Keyword, data)

    def movies(self, *, page: int = 1, include_adult: bool = False) -> schemas.Movies:
        """Get the movies that belong to a keyword.

        See more: https://developers.themoviedb.org/3/keywords/get-movies-by-keyword
        """
        data = self.request(f"keyword/{self.keyword_id}/movies", page=page, include_adult=include_adult)
        return utils.as_dataclass(schemas.Movies, data)
