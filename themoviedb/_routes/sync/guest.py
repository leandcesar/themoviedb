from typing import Optional

from themoviedb import schemas
from themoviedb._core._resource_state import _GuestResource
from themoviedb._endpoints.misc import (
    GUEST_RATED_EPISODES,
    GUEST_RATED_MOVIES,
    GUEST_RATED_TV,
)
from themoviedb._routes.sync._base import Base


class Guest(_GuestResource, Base):

    def rated_movies(self, *, sort_by: Optional[str] = None) -> schemas.RatedMovies:
        return self._request_endpoint(GUEST_RATED_MOVIES, path_params=self._path_params, sort_by=sort_by)

    def rated_tvs(self, *, sort_by: Optional[str] = None) -> schemas.RatedTVs:
        return self._request_endpoint(GUEST_RATED_TV, path_params=self._path_params, sort_by=sort_by)

    def rated_episodes(self, *, sort_by: Optional[str] = None) -> schemas.RatedEpisodes:
        return self._request_endpoint(GUEST_RATED_EPISODES, path_params=self._path_params, sort_by=sort_by)
