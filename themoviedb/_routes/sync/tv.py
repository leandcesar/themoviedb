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
from themoviedb._routes.sync._base import Base


class TV(_TVResource, Base):
    """Operations for one TV show."""

    def details(self, *, append_to_response: Optional[str] = None) -> schemas.TV:
        return self._request_endpoint(
            TV_DETAILS, path_params=self._path_params, append_to_response=append_to_response
        )

    def aggregate_credits(self) -> schemas.Credits:
        return self._request_endpoint(TV_AGGREGATE_CREDITS, path_params=self._path_params)

    def alternative_titles(self, *, country: Optional[str] = None) -> schemas.AlternativeTitles:
        return self._request_endpoint(TV_ALTERNATIVE_TITLES, path_params=self._path_params, country=country)

    def content_ratings(self) -> schemas.ContentRatings:
        return self._request_endpoint(TV_CONTENT_RATINGS, path_params=self._path_params)

    def credits(self) -> schemas.Credits:
        return self._request_endpoint(TV_CREDITS, path_params=self._path_params)

    def external_ids(self) -> schemas.ExternalIDs:
        return self._request_endpoint(TV_EXTERNAL_IDS, path_params=self._path_params)

    def episode_groups(self) -> schemas.EpisodeGroups:
        return self._request_endpoint(TV_EPISODE_GROUPS, path_params=self._path_params)

    def images(self) -> schemas.Images:
        return self._request_endpoint(TV_IMAGES, path_params=self._path_params)

    def keywords(self) -> schemas.Keywords:
        return self._request_endpoint(TV_KEYWORDS, path_params=self._path_params)

    def recommendations(self, *, page: int = 1) -> schemas.TVs:
        return self._request_endpoint(TV_RECOMMENDATIONS, path_params=self._path_params, page=page)

    def reviews(self, *, page: int = 1) -> schemas.Reviews:
        return self._request_endpoint(TV_REVIEWS, path_params=self._path_params, page=page)

    def screened_theatrically(self, *, page: int = 1) -> schemas.Episodes:
        return self._request_endpoint(TV_SCREENED_THEATRICALLY, path_params=self._path_params, page=page)

    def similar(self, *, page: int = 1) -> schemas.TVs:
        return self._request_endpoint(TV_SIMILAR, path_params=self._path_params, page=page)

    def translations(self) -> schemas.Translations:
        return self._request_endpoint(TV_TRANSLATIONS, path_params=self._path_params)

    def videos(self, *, page: int = 1) -> schemas.Videos:
        return self._request_endpoint(TV_VIDEOS, path_params=self._path_params, page=page)

    def watch_providers(self) -> schemas.WatchProviders:
        return self._request_endpoint(TV_WATCH_PROVIDERS, path_params=self._path_params)


class TVs(Base):
    """Operations for TV collections."""

    def latest(self) -> schemas.TV:
        return self._request_endpoint(TVS_LATEST)

    def airing_today(self, *, page: int = 1) -> schemas.TVs:
        return self._request_endpoint(TVS_AIRING_TODAY, page=page)

    def on_the_air(self, *, page: int = 1) -> schemas.TVs:
        return self._request_endpoint(TVS_ON_THE_AIR, page=page)

    def popular(self, *, page: int = 1) -> schemas.TVs:
        return self._request_endpoint(TVS_POPULAR, page=page)

    def top_rated(self, *, page: int = 1) -> schemas.TVs:
        return self._request_endpoint(TVS_TOP_RATED, page=page)
