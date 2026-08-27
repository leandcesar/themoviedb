from themoviedb import schemas
from themoviedb._core._resource_state import _ReviewResource
from themoviedb._endpoints.misc import REVIEW_DETAILS
from themoviedb._routes.async_._base import Base


class Review(_ReviewResource, Base):

    async def details(self) -> schemas.Review:
        return await self._request_endpoint(REVIEW_DETAILS, path_params=self._path_params)
