from typing import Optional

from themoviedb import schemas, utils
from themoviedb.routes_sync._base import Base


class WatchProviders(Base):

    def movie(self, watch_region: Optional[str] = None) -> schemas.WatchProvidersData:
        """Returns a list of the watch provider (OTT/streaming) data we have available for movies.

        See more: https://developers.themoviedb.org/3/watch-providers/get-movie-providers
        """
        data = self.request("watch/providers/movie", watch_region=watch_region)
        return utils.as_dataclass(schemas.WatchProvidersData, data)

    def regions(self) -> schemas.Regions:
        """Returns a list of all of the countries we have watch provider (OTT/streaming) data for.

        See more: https://developers.themoviedb.org/3/watch-providers/get-available-regions
        """
        data = self.request("watch/providers/regions")
        return utils.as_dataclass(schemas.Regions, data)

    def tv(self, watch_region: Optional[str] = None) -> schemas.WatchProvidersData:
        """Returns a list of the watch provider (OTT/streaming) data we have available for TV series.

        See more: https://developers.themoviedb.org/3/watch-providers/get-tv-providers
        """
        data = self.request("watch/providers/tv", watch_region=watch_region)
        return utils.as_dataclass(schemas.WatchProvidersData, data)
