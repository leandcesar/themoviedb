from themoviedb import schemas
from themoviedb._core._resource_state import _CompanyResource
from themoviedb._endpoints.resources import (
    COMPANY_ALTERNATIVE_NAMES,
    COMPANY_DETAILS,
    COMPANY_IMAGES,
)
from themoviedb._routes.sync._base import Base


class Company(_CompanyResource, Base):

    def details(self) -> schemas.Company:
        return self._request_endpoint(COMPANY_DETAILS, path_params=self._path_params)

    def alternative_names(self) -> schemas.AlternativeNames:
        return self._request_endpoint(COMPANY_ALTERNATIVE_NAMES, path_params=self._path_params)

    def images(self) -> schemas.Images:
        return self._request_endpoint(COMPANY_IMAGES, path_params=self._path_params)
