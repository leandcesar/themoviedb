# -*- coding: utf-8 -*-
from themoviedb import schemas, utils
from themoviedb.routes.base import Base


class Person(Base):
    def __init__(self, person_id: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.person_id = person_id

    async def details(self, *, append_to_response: str = None, image_language: str = "null") -> schemas.Person:
        """Get the primary person details by id.

        See more: https://developers.themoviedb.org/3/people/get-person-details
        """
        data = await self.request(f"person/{self.person_id}", append_to_response=append_to_response, include_image_language=image_language)
        return utils.as_dataclass(schemas.Person, data)

    async def external_ids(self) -> schemas.ExternalIDs:
        """Get the external ids for a person.

        See more: https://developers.themoviedb.org/3/people/get-person-external-ids
        """
        data = await self.request(f"person/{self.person_id}/external_ids")
        return utils.as_dataclass(schemas.ExternalIDs, data)

    async def images(self) -> schemas.Images:
        """Get the images for a person.

        See more: https://developers.themoviedb.org/3/people/get-person-images
        """
        data = await self.request(f"person/{self.person_id}/images")
        return utils.as_dataclass(schemas.Images, data)

    async def combined_credits(self) -> schemas.CreditsCombined:
        """Get the movie and TV credits together in a single response.

        See more: https://developers.themoviedb.org/3/people/get-person-combined-credits
        """
        data = await self.request(f"person/{self.person_id}/combined_credits")
        return utils.as_dataclass(schemas.CreditsCombined, data)

    async def movie_credits(self) -> schemas.CreditsMovie:
        """Get the movie credits for a person.

        See more: https://developers.themoviedb.org/3/people/get-person-movie-credits
        """
        data = await self.request(f"person/{self.person_id}/movie_credits")
        return utils.as_dataclass(schemas.CreditsMovie, data)

    async def tv_credits(self) -> schemas.CreditsTV:
        """Get the TV show credits for a person.

        See more: https://developers.themoviedb.org/3/people/get-person-tv-credits
        """
        data = await self.request(f"person/{self.person_id}/tv_credits")
        return utils.as_dataclass(schemas.CreditsTV, data)

    async def tagged_images(self) -> schemas.TaggedImages:
        """Get the images that this person has been tagged in.

        See more: https://developers.themoviedb.org/3/people/get-tagged-images
        """
        data = await self.request(f"person/{self.person_id}/tagged_images")
        return utils.as_dataclass(schemas.TaggedImages, data)

    async def translations(self) -> schemas.Translations:
        """Get a list of translations that have been created for a person.

        See more: https://developers.themoviedb.org/3/people/get-person-translations
        """
        data = await self.request(f"person/{self.person_id}/translations")
        return utils.as_dataclass(schemas.Translations, data)


class People(Base):

    async def latest(self) -> schemas.Person:
        """Get the most newly created person.

        See more: https://developers.themoviedb.org/3/people/get-latest-person
        """
        data = await self.request("person/latest")
        return utils.as_dataclass(schemas.Person, data)

    async def popular(self, *, page: int = 1) -> schemas.People:
        """Get the list of popular people on TMDB.

        See more: https://developers.themoviedb.org/3/people/get-popular-people
        """
        data = await self.request("person/popular", page=page)
        return utils.as_dataclass(schemas.People, data)
