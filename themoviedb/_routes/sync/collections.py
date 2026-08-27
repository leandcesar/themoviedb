from themoviedb import schemas
from themoviedb._core._resource_state import _CollectionResource
from themoviedb._endpoints.resources import (
    COLLECTION_DETAILS,
    COLLECTION_IMAGES,
    COLLECTION_TRANSLATIONS,
)
from themoviedb._routes.sync._base import Base


class Collection(_CollectionResource, Base):

    def details(self) -> schemas.Collection:
        return self._request_endpoint(COLLECTION_DETAILS, path_params=self._path_params)

    def images(self) -> schemas.Images:
        return self._request_endpoint(COLLECTION_IMAGES, path_params=self._path_params)

    def translations(self) -> schemas.Translations:
        return self._request_endpoint(COLLECTION_TRANSLATIONS, path_params=self._path_params)
