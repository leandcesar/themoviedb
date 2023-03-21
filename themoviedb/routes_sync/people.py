from typing import Optional

from themoviedb import schemas, utils
from themoviedb.routes_sync._base import Base


class Person(Base):
    def __init__(self, person_id: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.person_id = person_id

    def details(self, *, append_to_response: Optional[str] = None, image_language: str = "null") -> schemas.Person:
        """Get the primary person details by id.

        See more: https://developers.themoviedb.org/3/people/get-person-details
        """
        data = self.request(f"person/{self.person_id}", append_to_response=append_to_response, include_image_language=image_language)
        return utils.as_dataclass(schemas.Person, data)

    def external_ids(self) -> schemas.ExternalIDs:
        """Get the external ids for a person.

        See more: https://developers.themoviedb.org/3/people/get-person-external-ids
        """
        data = self.request(f"person/{self.person_id}/external_ids")
        return utils.as_dataclass(schemas.ExternalIDs, data)

    def images(self) -> schemas.Images:
        """Get the images for a person.

        See more: https://developers.themoviedb.org/3/people/get-person-images
        """
        data = self.request(f"person/{self.person_id}/images")
        return utils.as_dataclass(schemas.Images, data)

    def combined_credits(self) -> schemas.CreditsCombined:
        """Get the movie and TV credits together in a single response.

        See more: https://developers.themoviedb.org/3/people/get-person-combined-credits
        """
        data = self.request(f"person/{self.person_id}/combined_credits")
        return utils.as_dataclass(schemas.CreditsCombined, data)

    def movie_credits(self) -> schemas.CreditsMovie:
        """Get the movie credits for a person.

        See more: https://developers.themoviedb.org/3/people/get-person-movie-credits
        """
        data = self.request(f"person/{self.person_id}/movie_credits")
        return utils.as_dataclass(schemas.CreditsMovie, data)

    def tv_credits(self) -> schemas.CreditsTV:
        """Get the TV show credits for a person.

        See more: https://developers.themoviedb.org/3/people/get-person-tv-credits
        """
        data = self.request(f"person/{self.person_id}/tv_credits")
        return utils.as_dataclass(schemas.CreditsTV, data)

    def tagged_images(self) -> schemas.TaggedImages:
        """Get the images that this person has been tagged in.

        See more: https://developers.themoviedb.org/3/people/get-tagged-images
        """
        data = self.request(f"person/{self.person_id}/tagged_images")
        return utils.as_dataclass(schemas.TaggedImages, data)

    def translations(self) -> schemas.Translations:
        """Get a list of translations that have been created for a person.

        See more: https://developers.themoviedb.org/3/people/get-person-translations
        """
        data = self.request(f"person/{self.person_id}/translations")
        return utils.as_dataclass(schemas.Translations, data)


class People(Base):

    def latest(self) -> schemas.Person:
        """Get the most newly created person.

        See more: https://developers.themoviedb.org/3/people/get-latest-person
        """
        data = self.request("person/latest")
        return utils.as_dataclass(schemas.Person, data)

    def popular(self, *, page: int = 1) -> schemas.People:
        """Get the list of popular people on TMDB.

        See more: https://developers.themoviedb.org/3/people/get-popular-people
        """
        data = self.request("person/popular", page=page)
        return utils.as_dataclass(schemas.People, data)
