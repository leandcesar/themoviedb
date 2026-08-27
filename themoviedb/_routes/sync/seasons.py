from typing import Optional

from themoviedb import schemas
from themoviedb._core._resource_state import _SeasonResource
from themoviedb._endpoints.resources import (
    SEASON_AGGREGATE_CREDITS,
    SEASON_CREDITS,
    SEASON_DETAILS,
    SEASON_EXTERNAL_IDS,
    SEASON_IMAGES,
    SEASON_TRANSLATIONS,
    SEASON_VIDEOS,
)
from themoviedb._routes.sync._base import Base


class Season(_SeasonResource, Base):

    def details(self, *, append_to_response: Optional[str] = None) -> schemas.Season:
        return self._request_endpoint(
            SEASON_DETAILS, path_params=self._path_params, append_to_response=append_to_response
        )

    def aggregate_credits(self) -> schemas.Credits:
        return self._request_endpoint(SEASON_AGGREGATE_CREDITS, path_params=self._path_params)

    def credits(self) -> schemas.Credits:
        return self._request_endpoint(SEASON_CREDITS, path_params=self._path_params)

    def external_ids(self) -> schemas.ExternalIDs:
        return self._request_endpoint(SEASON_EXTERNAL_IDS, path_params=self._path_params)

    def images(self) -> schemas.Images:
        return self._request_endpoint(SEASON_IMAGES, path_params=self._path_params)

    def translations(self) -> schemas.Translations:
        return self._request_endpoint(SEASON_TRANSLATIONS, path_params=self._path_params)

    def videos(self) -> schemas.Videos:
        return self._request_endpoint(SEASON_VIDEOS, path_params=self._path_params)
