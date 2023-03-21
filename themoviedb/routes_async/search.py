from typing import Optional

from themoviedb import schemas, utils
from themoviedb.routes_async._base import Base


class Search(Base):

    async def companies(self, query: str, *, page: int = 1) -> schemas.Companies:
        """Search for companies.

        See more: https://developers.themoviedb.org/3/search/search-companies
        """
        data = await self.request("search/company", query=query, page=page)
        return utils.as_dataclass(schemas.Companies, data)

    async def collections(self, query: str, *, page: int = 1) -> schemas.Collections:
        """Search for collections.

        See more: https://developers.themoviedb.org/3/search/search-collections
        """
        data = await self.request("search/collection", query=query, page=page)
        return utils.as_dataclass(schemas.Collections, data)

    async def keywords(self, query: str, *, page: int = 1) -> schemas.Keywords:
        """Search for keywords.

        See more: https://developers.themoviedb.org/3/search/search-keywords
        """
        data = await self.request("search/keyword", query=query, page=page)
        return utils.as_dataclass(schemas.Keywords, data)

    async def movies(
        self,
        query: str,
        *,
        page: int = 1,
        include_adult: bool = False,
        year: Optional[int] = None,
        primary_release_year: Optional[int] = None,
    ) -> schemas.Movies:
        """Search for movies.

        See more: https://developers.themoviedb.org/3/search/search-movies
        """
        data = await self.request(
            "search/movie",
            query=query,
            page=page,
            include_adult=include_adult,
            year=year,
            primary_release_year=primary_release_year,
        )
        return utils.as_dataclass(schemas.Movies, data)

    async def multi(self, query: str, *, page: int = 1, include_adult: bool = False) -> schemas.Multis:
        """Search multiple models in a single request. Multi search currently
        supports searching for movies, tv shows and people in a single request.

        See more: https://developers.themoviedb.org/3/search/multi-search
        """
        data = await self.request("search/multi", query=query, page=page, include_adult=include_adult)
        return utils.as_dataclass(schemas.Multis, data)

    async def people(self, query: str, *, page: int = 1, include_adult: bool = False) -> schemas.People:
        """Search for people.

        See more: https://developers.themoviedb.org/3/search/search-people
        """
        data = await self.request("search/person", query=query, page=page, include_adult=include_adult)
        return utils.as_dataclass(schemas.People, data)

    async def tv(
        self,
        query: str,
        *,
        page: int = 1,
        include_adult: bool = False,
        first_air_date_year: Optional[int] = None,
    ) -> schemas.TVs:
        """Search for a TV show.

        See more: https://developers.themoviedb.org/3/search/search-tv-shows
        """
        data = await self.request(
            "search/tv",
            query=query,
            page=page,
            include_adult=include_adult,
            first_air_date_year=first_air_date_year,
        )
        return utils.as_dataclass(schemas.TVs, data)
