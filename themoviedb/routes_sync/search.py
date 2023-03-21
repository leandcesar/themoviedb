from typing import Optional

from themoviedb import schemas, utils
from themoviedb.routes_sync._base import Base


class Search(Base):

    def companies(self, query: str, *, page: int = 1) -> schemas.Companies:
        """Search for companies.

        See more: https://developers.themoviedb.org/3/search/search-companies
        """
        data = self.request("search/company", query=query, page=page)
        return utils.as_dataclass(schemas.Companies, data)

    def collections(self, query: str, *, page: int = 1) -> schemas.Collections:
        """Search for collections.

        See more: https://developers.themoviedb.org/3/search/search-collections
        """
        data = self.request("search/collection", query=query, page=page)
        return utils.as_dataclass(schemas.Collections, data)

    def keywords(self, query: str, *, page: int = 1) -> schemas.Keywords:
        """Search for keywords.

        See more: https://developers.themoviedb.org/3/search/search-keywords
        """
        data = self.request("search/keyword", query=query, page=page)
        return utils.as_dataclass(schemas.Keywords, data)

    def movies(
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
        data = self.request(
            "search/movie",
            query=query,
            page=page,
            include_adult=include_adult,
            year=year,
            primary_release_year=primary_release_year,
        )
        return utils.as_dataclass(schemas.Movies, data)

    def multi(self, query: str, *, page: int = 1, include_adult: bool = False) -> schemas.Multis:
        """Search multiple models in a single request. Multi search currently
        supports searching for movies, tv shows and people in a single request.

        See more: https://developers.themoviedb.org/3/search/multi-search
        """
        data = self.request("search/multi", query=query, page=page, include_adult=include_adult)
        return utils.as_dataclass(schemas.Multis, data)

    def people(self, query: str, *, page: int = 1, include_adult: bool = False) -> schemas.People:
        """Search for people.

        See more: https://developers.themoviedb.org/3/search/search-people
        """
        data = self.request("search/person", query=query, page=page, include_adult=include_adult)
        return utils.as_dataclass(schemas.People, data)

    def tv(
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
        data = self.request(
            "search/tv",
            query=query,
            page=page,
            include_adult=include_adult,
            first_air_date_year=first_air_date_year,
        )
        return utils.as_dataclass(schemas.TVs, data)
