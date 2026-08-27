from themoviedb import schemas
from themoviedb._core._resource_state import _CreditResource
from themoviedb._endpoints.resources import CREDIT_DETAILS
from themoviedb._routes.async_._base import Base


class Credit(_CreditResource, Base):

    async def details(self) -> schemas.Credit:
        return await self._request_endpoint(CREDIT_DETAILS, path_params=self._path_params)
