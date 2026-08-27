from themoviedb import schemas
from themoviedb._core._resource_state import _NetworkResource
from themoviedb._endpoints.resources import (
    NETWORK_ALTERNATIVE_NAMES,
    NETWORK_DETAILS,
    NETWORK_IMAGES,
)
from themoviedb._routes.async_._base import Base


class Network(_NetworkResource, Base):

    async def details(self) -> schemas.Network:
        return await self._request_endpoint(NETWORK_DETAILS, path_params=self._path_params)

    async def alternative_names(self) -> schemas.AlternativeNames:
        return await self._request_endpoint(NETWORK_ALTERNATIVE_NAMES, path_params=self._path_params)

    async def images(self) -> schemas.Images:
        return await self._request_endpoint(NETWORK_IMAGES, path_params=self._path_params)
