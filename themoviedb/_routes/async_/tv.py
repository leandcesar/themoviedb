from typing import Optional

from themoviedb import schemas
from themoviedb._core._resource_state import _TVResource
from themoviedb._endpoints.tv import (
    TV_AGGREGATE_CREDITS,
    TV_ALTERNATIVE_TITLES,
    TV_CONTENT_RATINGS,
    TV_CREDITS,
    TV_DETAILS,
    TV_EPISODE_GROUPS,
    TV_EXTERNAL_IDS,
    TV_IMAGES,
    TV_KEYWORDS,
    TV_RECOMMENDATIONS,
    TV_REVIEWS,
    TV_SCREENED_THEATRICALLY,
    TV_SIMILAR,
    TV_TRANSLATIONS,
    TV_VIDEOS,
    TV_WATCH_PROVIDERS,
    TVS_AIRING_TODAY,
    TVS_LATEST,
    TVS_ON_THE_AIR,
    TVS_POPULAR,
    TVS_TOP_RATED,
)
from themoviedb._routes.async_._base import Base


class TV(_TVResource, Base):
    """Operations for one TV show."""

    async def details(self, *, append_to_response: Optional[str] = None) -> schemas.TV:
        return await self._request_endpoint(
            TV_DETAILS, path_params=self._path_params, append_to_response=append_to_response
        )

    async def aggregate_credits(self) -> schemas.Credits:
        return await self._request_endpoint(TV_AGGREGATE_CREDITS, path_params=self._path_params)

    async def alternative_titles(self, *, country: Optional[str] = None) -> schemas.AlternativeTitles:
        return await self._request_endpoint(TV_ALTERNATIVE_TITLES, path_params=self._path_params, country=country)

    async def content_ratings(self) -> schemas.ContentRatings:
        return await self._request_endpoint(TV_CONTENT_RATINGS, path_params=self._path_params)

    async def credits(self) -> schemas.Credits:
        return await self._request_endpoint(TV_CREDITS, path_params=self._path_params)

    async def external_ids(self) -> schemas.ExternalIDs:
        return await self._request_endpoint(TV_EXTERNAL_IDS, path_params=self._path_params)

    async def episode_groups(self) -> schemas.EpisodeGroups:
        return await self._request_endpoint(TV_EPISODE_GROUPS, path_params=self._path_params)

    async def images(self) -> schemas.Images:
        return await self._request_endpoint(TV_IMAGES, path_params=self._path_params)

    async def keywords(self) -> schemas.Keywords:
        return await self._request_endpoint(TV_KEYWORDS, path_params=self._path_params)

    async def recommendations(self, *, page: int = 1) -> schemas.TVs:
        return await self._request_endpoint(TV_RECOMMENDATIONS, path_params=self._path_params, page=page)

    async def reviews(self, *, page: int = 1) -> schemas.Reviews:
        return await self._request_endpoint(TV_REVIEWS, path_params=self._path_params, page=page)

    async def screened_theatrically(self, *, page: int = 1) -> schemas.Episodes:
        return await self._request_endpoint(TV_SCREENED_THEATRICALLY, path_params=self._path_params, page=page)

    async def similar(self, *, page: int = 1) -> schemas.TVs:
        return await self._request_endpoint(TV_SIMILAR, path_params=self._path_params, page=page)

    async def translations(self) -> schemas.Translations:
        return await self._request_endpoint(TV_TRANSLATIONS, path_params=self._path_params)

    async def videos(self, *, page: int = 1) -> schemas.Videos:
        return await self._request_endpoint(TV_VIDEOS, path_params=self._path_params, page=page)

    async def watch_providers(self) -> schemas.WatchProviders:
        return await self._request_endpoint(TV_WATCH_PROVIDERS, path_params=self._path_params)


class TVs(Base):
    """Operations for TV collections."""

    async def latest(self) -> schemas.TV:
        return await self._request_endpoint(TVS_LATEST)

    async def airing_today(self, *, page: int = 1) -> schemas.TVs:
        return await self._request_endpoint(TVS_AIRING_TODAY, page=page)

    async def on_the_air(self, *, page: int = 1) -> schemas.TVs:
        return await self._request_endpoint(TVS_ON_THE_AIR, page=page)

    async def popular(self, *, page: int = 1) -> schemas.TVs:
        return await self._request_endpoint(TVS_POPULAR, page=page)

    async def top_rated(self, *, page: int = 1) -> schemas.TVs:
        return await self._request_endpoint(TVS_TOP_RATED, page=page)
