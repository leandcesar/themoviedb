from typing import Optional

from themoviedb import schemas
from themoviedb._endpoints.misc import (
    WATCH_PROVIDERS_MOVIE,
    WATCH_PROVIDERS_REGIONS,
    WATCH_PROVIDERS_TV,
)
from themoviedb._routes.sync._base import Base


class WatchProviders(Base):
    def movie(self, watch_region: Optional[str] = None) -> schemas.WatchProvidersData:
        return self._request_endpoint(WATCH_PROVIDERS_MOVIE, watch_region=watch_region)

    def regions(self) -> schemas.Regions:
        return self._request_endpoint(WATCH_PROVIDERS_REGIONS)

    def tv(self, watch_region: Optional[str] = None) -> schemas.WatchProvidersData:
        return self._request_endpoint(WATCH_PROVIDERS_TV, watch_region=watch_region)
