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
from themoviedb._routes.async_._base import Base


class Episode(_EpisodeResource, Base):

    async def details(self, *, append_to_response: Optional[str] = None) -> schemas.Episode:
        return await self._request_endpoint(
            EPISODE_DETAILS, path_params=self._path_params, append_to_response=append_to_response
        )

    async def credits(self) -> schemas.Credits:
        return await self._request_endpoint(EPISODE_CREDITS, path_params=self._path_params)

    async def external_ids(self) -> schemas.ExternalIDs:
        return await self._request_endpoint(EPISODE_EXTERNAL_IDS, path_params=self._path_params)

    async def images(self) -> schemas.Images:
        return await self._request_endpoint(EPISODE_IMAGES, path_params=self._path_params)

    async def translations(self) -> schemas.Translations:
        return await self._request_endpoint(EPISODE_TRANSLATIONS, path_params=self._path_params)

    async def videos(self) -> schemas.Videos:
        return await self._request_endpoint(EPISODE_VIDEOS, path_params=self._path_params)
