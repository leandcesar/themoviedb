from typing import Optional

from themoviedb import schemas
from themoviedb._core._resource_state import _PersonResource
from themoviedb._endpoints.people import (
    PEOPLE_LATEST,
    PEOPLE_POPULAR,
    PERSON_COMBINED_CREDITS,
    PERSON_DETAILS,
    PERSON_EXTERNAL_IDS,
    PERSON_IMAGES,
    PERSON_MOVIE_CREDITS,
    PERSON_TAGGED_IMAGES,
    PERSON_TRANSLATIONS,
    PERSON_TV_CREDITS,
)
from themoviedb._routes.sync._base import Base


class Person(_PersonResource, Base):
    """Operations for one person."""

    def details(self, *, append_to_response: Optional[str] = None, image_language: str = "null") -> schemas.Person:
        return self._request_endpoint(
            PERSON_DETAILS,
            path_params=self._path_params,
            append_to_response=append_to_response,
            include_image_language=image_language,
        )

    def external_ids(self) -> schemas.ExternalIDs:
        return self._request_endpoint(PERSON_EXTERNAL_IDS, path_params=self._path_params)

    def images(self) -> schemas.Images:
        return self._request_endpoint(PERSON_IMAGES, path_params=self._path_params)

    def combined_credits(self) -> schemas.CreditsCombined:
        return self._request_endpoint(PERSON_COMBINED_CREDITS, path_params=self._path_params)

    def movie_credits(self) -> schemas.CreditsMovie:
        return self._request_endpoint(PERSON_MOVIE_CREDITS, path_params=self._path_params)

    def tv_credits(self) -> schemas.CreditsTV:
        return self._request_endpoint(PERSON_TV_CREDITS, path_params=self._path_params)

    def tagged_images(self) -> schemas.TaggedImages:
        return self._request_endpoint(PERSON_TAGGED_IMAGES, path_params=self._path_params)

    def translations(self) -> schemas.Translations:
        return self._request_endpoint(PERSON_TRANSLATIONS, path_params=self._path_params)


class People(Base):
    """Operations for people collections."""

    def latest(self) -> schemas.Person:
        return self._request_endpoint(PEOPLE_LATEST)

    def popular(self, *, page: int = 1) -> schemas.People:
        return self._request_endpoint(PEOPLE_POPULAR, page=page)
