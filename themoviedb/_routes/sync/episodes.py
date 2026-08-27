from typing import Optional

from themoviedb import schemas
from themoviedb._core._resource_state import _EpisodeResource
from themoviedb._endpoints.resources import (
    EPISODE_CREDITS,
    EPISODE_DETAILS,
    EPISODE_EXTERNAL_IDS,
    EPISODE_IMAGES,
    EPISODE_TRANSLATIONS,
    EPISODE_VIDEOS,
)
from themoviedb._routes.sync._base import Base


class Episode(_EpisodeResource, Base):

    def details(self, *, append_to_response: Optional[str] = None) -> schemas.Episode:
        return self._request_endpoint(
            EPISODE_DETAILS, path_params=self._path_params, append_to_response=append_to_response
        )

    def credits(self) -> schemas.Credits:
        return self._request_endpoint(EPISODE_CREDITS, path_params=self._path_params)

    def external_ids(self) -> schemas.ExternalIDs:
        return self._request_endpoint(EPISODE_EXTERNAL_IDS, path_params=self._path_params)

    def images(self) -> schemas.Images:
        return self._request_endpoint(EPISODE_IMAGES, path_params=self._path_params)

    def translations(self) -> schemas.Translations:
        return self._request_endpoint(EPISODE_TRANSLATIONS, path_params=self._path_params)

    def videos(self) -> schemas.Videos:
        return self._request_endpoint(EPISODE_VIDEOS, path_params=self._path_params)
