from typing import Optional

from themoviedb import schemas
from themoviedb._endpoints.search import (
    SEARCH_COLLECTIONS,
    SEARCH_COMPANIES,
    SEARCH_KEYWORDS,
    SEARCH_MOVIES,
    SEARCH_MULTI,
    SEARCH_PEOPLE,
    SEARCH_TV,
)
from themoviedb._routes.sync._base import Base


class Search(Base):
    """Search TMDb resources."""

    def companies(self, query: str, *, page: int = 1) -> schemas.Companies:
        return self._request_endpoint(SEARCH_COMPANIES, query=query, page=page)

    def collections(self, query: str, *, page: int = 1) -> schemas.Collections:
        return self._request_endpoint(SEARCH_COLLECTIONS, query=query, page=page)

    def keywords(self, query: str, *, page: int = 1) -> schemas.Keywords:
        return self._request_endpoint(SEARCH_KEYWORDS, query=query, page=page)

    def movies(
        self,
        query: str,
        *,
        page: int = 1,
        include_adult: bool = False,
        year: Optional[int] = None,
        primary_release_year: Optional[int] = None,
    ) -> schemas.Movies:
        return self._request_endpoint(
            SEARCH_MOVIES,
            query=query,
            page=page,
            include_adult=include_adult,
            year=year,
            primary_release_year=primary_release_year,
        )

    def multi(self, query: str, *, page: int = 1, include_adult: bool = False) -> schemas.Multis:
        return self._request_endpoint(SEARCH_MULTI, query=query, page=page, include_adult=include_adult)

    def people(self, query: str, *, page: int = 1, include_adult: bool = False) -> schemas.People:
        return self._request_endpoint(SEARCH_PEOPLE, query=query, page=page, include_adult=include_adult)

    def tv(
        self,
        query: str,
        *,
        page: int = 1,
        include_adult: bool = False,
        first_air_date_year: Optional[int] = None,
    ) -> schemas.TVs:
        return self._request_endpoint(
            SEARCH_TV,
            query=query,
            page=page,
            include_adult=include_adult,
            first_air_date_year=first_air_date_year,
        )
