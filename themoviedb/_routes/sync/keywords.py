from themoviedb import schemas
from themoviedb._core._resource_state import _KeywordResource
from themoviedb._endpoints.misc import KEYWORD_DETAILS, KEYWORD_MOVIES
from themoviedb._routes.sync._base import Base


class Keyword(_KeywordResource, Base):

    def details(self) -> schemas.Keyword:
        return self._request_endpoint(KEYWORD_DETAILS, path_params=self._path_params)

    def movies(self, *, page: int = 1, include_adult: bool = False) -> schemas.Movies:
        return self._request_endpoint(
            KEYWORD_MOVIES, path_params=self._path_params, page=page, include_adult=include_adult
        )
