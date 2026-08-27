from themoviedb import schemas
from themoviedb._core._resource_state import _CollectionResource
from themoviedb._endpoints.resources import (
    COLLECTION_DETAILS,
    COLLECTION_IMAGES,
    COLLECTION_TRANSLATIONS,
)
from themoviedb._routes.async_._base import Base


class Collection(_CollectionResource, Base):

    async def details(self) -> schemas.Collection:
        return await self._request_endpoint(COLLECTION_DETAILS, path_params=self._path_params)

    async def images(self) -> schemas.Images:
        return await self._request_endpoint(COLLECTION_IMAGES, path_params=self._path_params)

    async def translations(self) -> schemas.Translations:
        return await self._request_endpoint(COLLECTION_TRANSLATIONS, path_params=self._path_params)
