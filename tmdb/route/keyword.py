# -*- coding: utf-8 -*-
from .base import Base, Response


class Keyword(Base):
    async def details(self, keyword_id: int) -> Response:
        """Get a keyword details by id.

        See more: https://developers.themoviedb.org/3/keywords/get-keyword-details
        """
        return await self.request(f"keyword/{keyword_id}")

    async def search(self, query: str, *, page: int = 1) -> Response:
        """Search for keywords.

        See more: https://developers.themoviedb.org/3/search/search-keywords
        """
        return await self.request("search/keyword", query=query, page=page)
