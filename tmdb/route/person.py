# -*- coding: utf-8 -*-
from .base import Base, Response


class Person(Base):
    async def details(self, person_id: int, *, append: str = None, image_language: str = "null") -> Response:
        """Get the primary person details by id.

        See more: https://developers.themoviedb.org/3/people/get-person-details
        """
        return await self.request(f"person/{person_id}", append_to_response=append, include_image_language=image_language)

    async def changes(self, person_id: int, *, start_date: str = None, end_date: str = None, page: int = 1) -> Response:
        """Get the changes for a person.

        See more: https://developers.themoviedb.org/3/people/get-person-changes
        """
        return await self.request(f"person/{person_id}/changes", start_date=start_date, end_date=end_date, page=page)

    async def movie_credits(self, person_id: int) -> Response:
        """Get the movie credits for a person.

        See more: https://developers.themoviedb.org/3/people/get-person-movie-credits
        """
        return await self.request(f"person/{person_id}/movie_credits")

    async def tv_credits(self, person_id: int) -> Response:
        """Get the TV show credits for a person.

        See more: https://developers.themoviedb.org/3/people/get-person-tv-credits
        """
        return await self.request(f"person/{person_id}/tv_credits")

    async def combined_credits(self, person_id: int) -> Response:
        """Get the movie and TV credits together in a single response.

        See more: https://developers.themoviedb.org/3/people/get-person-combined-credits
        """
        return await self.request(f"person/{person_id}/combined_credits")

    async def external_ids(self, person_id: int) -> Response:
        """Get the external ids for a person.

        See more: https://developers.themoviedb.org/3/people/get-person-external-ids
        """
        return await self.request(f"person/{person_id}/external_ids")

    async def images(self, person_id: int) -> Response:
        """Get the images for a person.

        See more: https://developers.themoviedb.org/3/people/get-person-images
        """
        return await self.request(f"person/{person_id}/images")

    async def tagged_images(self, person_id: int, *, page: int = 1) -> Response:
        """Get the images that this person has been tagged in.

        See more: https://developers.themoviedb.org/3/people/get-tagged-images
        """
        return await self.request(f"person/{person_id}/tagged_images", page=page)

    async def keywords(self, person_id: int) -> Response:
        """Get the keywords that have been added to a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-keywords
        """
        return await self.request(f"person/{person_id}/keywords")

    async def latest(self) -> Response:
        """Get the most newly created person.

        See more: https://developers.themoviedb.org/3/people/get-latest-person
        """
        return await self.request("person/latest")

    async def popular(self, *, page: int = 1) -> Response:
        """Get the list of popular people on TMDB.

        See more: https://developers.themoviedb.org/3/people/get-popular-people
        """
        return await self.request("person/popular", page=page)

    async def search(
        self, query: str, *, page: int = 1, include_adult: bool = False
    ) -> Response:
        """Search for people.

        See more: https://developers.themoviedb.org/3/search/search-people
        """
        return await self.request("search/person", query=query, page=page, include_adult=include_adult)

    async def translations(self, person_id: int) -> Response:
        """Get a list of translations that have been created for a person.

        See more: https://developers.themoviedb.org/3/people/get-person-translations
        """
        return await self.request(f"person/{person_id}/translations")

    async def trending(self, *, interval: str = "day", page: int = 1) -> Response:
        """Get the daily (`interval=day`) or weekly (`interval=week`) trending TV shows.

        See more: https://developers.themoviedb.org/3/trending/get-trending
        """
        return await self.request(f"trending/person/{interval}", page=page)
