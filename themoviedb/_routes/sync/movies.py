from typing import Optional

from themoviedb import schemas
from themoviedb._core._resource_state import _MovieResource
from themoviedb._endpoints.movies import (
    MOVIE_ALTERNATIVE_TITLES,
    MOVIE_CREDITS,
    MOVIE_DETAILS,
    MOVIE_EXTERNAL_IDS,
    MOVIE_IMAGES,
    MOVIE_KEYWORDS,
    MOVIE_LISTS,
    MOVIE_RECOMMENDATIONS,
    MOVIE_RELEASE_DATES,
    MOVIE_REVIEWS,
    MOVIE_SIMILAR,
    MOVIE_TRANSLATIONS,
    MOVIE_VIDEOS,
    MOVIE_WATCH_PROVIDERS,
    MOVIES_LATEST,
    MOVIES_NOW_PLAYING,
    MOVIES_POPULAR,
    MOVIES_TOP_RATED,
    MOVIES_UPCOMING,
)
from themoviedb._routes.sync._base import Base


class Movie(_MovieResource, Base):
    """Operations for one movie."""

    def details(self, *, append_to_response: Optional[str] = None, image_language: str = "null") -> schemas.Movie:
        return self._request_endpoint(
            MOVIE_DETAILS,
            path_params=self._path_params,
            append_to_response=append_to_response,
            include_image_language=image_language,
        )

    def alternative_titles(self, *, country: Optional[str] = None) -> schemas.AlternativeTitles:
        return self._request_endpoint(MOVIE_ALTERNATIVE_TITLES, path_params=self._path_params, country=country)

    def credits(self) -> schemas.Credits:
        return self._request_endpoint(MOVIE_CREDITS, path_params=self._path_params)

    def external_ids(self) -> schemas.ExternalIDs:
        return self._request_endpoint(MOVIE_EXTERNAL_IDS, path_params=self._path_params)

    def keywords(self) -> schemas.Keywords:
        return self._request_endpoint(MOVIE_KEYWORDS, path_params=self._path_params)

    def images(self, *, include_image_language: Optional[str] = None) -> schemas.Images:
        return self._request_endpoint(
            MOVIE_IMAGES,
            path_params=self._path_params,
            include_image_language=include_image_language,
        )

    def lists(self, *, page: int = 1) -> schemas.ItemsList:
        return self._request_endpoint(MOVIE_LISTS, path_params=self._path_params, page=page)

    def recommendations(self, *, page: int = 1) -> schemas.Movies:
        return self._request_endpoint(MOVIE_RECOMMENDATIONS, path_params=self._path_params, page=page)

    def release_dates(self) -> schemas.ReleaseDates:
        return self._request_endpoint(MOVIE_RELEASE_DATES, path_params=self._path_params)

    def reviews(self, *, page: int = 1) -> schemas.Reviews:
        return self._request_endpoint(MOVIE_REVIEWS, path_params=self._path_params, page=page)

    def similar(self, *, page: int = 1) -> schemas.Movies:
        return self._request_endpoint(MOVIE_SIMILAR, path_params=self._path_params, page=page)

    def translations(self) -> schemas.Translations:
        return self._request_endpoint(MOVIE_TRANSLATIONS, path_params=self._path_params)

    def videos(self, *, page: int = 1) -> schemas.Videos:
        return self._request_endpoint(MOVIE_VIDEOS, path_params=self._path_params, page=page)

    def watch_providers(self) -> schemas.WatchProviders:
        return self._request_endpoint(MOVIE_WATCH_PROVIDERS, path_params=self._path_params)


class Movies(Base):
    """Operations for movie collections."""

    def latest(self) -> schemas.Movie:
        return self._request_endpoint(MOVIES_LATEST)

    def now_playing(self, *, page: int = 1) -> schemas.Movies:
        return self._request_endpoint(MOVIES_NOW_PLAYING, page=page)

    def popular(self, *, page: int = 1) -> schemas.Movies:
        return self._request_endpoint(MOVIES_POPULAR, page=page)

    def top_rated(self, *, page: int = 1) -> schemas.Movies:
        return self._request_endpoint(MOVIES_TOP_RATED, page=page)

    def upcoming(self, *, page: int = 1) -> schemas.Movies:
        return self._request_endpoint(MOVIES_UPCOMING, page=page)
