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
from themoviedb._routes.async_._base import Base


class Season(_SeasonResource, Base):

    async def details(self, *, append_to_response: Optional[str] = None) -> schemas.Season:
        return await self._request_endpoint(
            SEASON_DETAILS, path_params=self._path_params, append_to_response=append_to_response
        )

    async def aggregate_credits(self) -> schemas.Credits:
        return await self._request_endpoint(SEASON_AGGREGATE_CREDITS, path_params=self._path_params)

    async def credits(self) -> schemas.Credits:
        return await self._request_endpoint(SEASON_CREDITS, path_params=self._path_params)

    async def external_ids(self) -> schemas.ExternalIDs:
        return await self._request_endpoint(SEASON_EXTERNAL_IDS, path_params=self._path_params)

    async def images(self) -> schemas.Images:
        return await self._request_endpoint(SEASON_IMAGES, path_params=self._path_params)

    async def translations(self) -> schemas.Translations:
        return await self._request_endpoint(SEASON_TRANSLATIONS, path_params=self._path_params)

    async def videos(self) -> schemas.Videos:
        return await self._request_endpoint(SEASON_VIDEOS, path_params=self._path_params)
