from themoviedb import schemas
from themoviedb._core._resource_state import _EpisodeGroupResource
from themoviedb._endpoints.misc import EPISODE_GROUP_DETAILS
from themoviedb._routes.sync._base import Base


class EpisodeGroup(_EpisodeGroupResource, Base):

    def details(self) -> schemas.EpisodeGroup:
        return self._request_endpoint(EPISODE_GROUP_DETAILS, path_params=self._path_params)
