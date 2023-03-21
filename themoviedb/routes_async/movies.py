from typing import Optional

from themoviedb import schemas, utils
from themoviedb.routes_async._base import Base


class Movie(Base):
    def __init__(self, movie_id: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.movie_id = movie_id

    async def details(self, *, append_to_response: Optional[str] = None, image_language: str = "null") -> schemas.Movie:
        """Get the primary information about a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-details
        """
        data = await self.request(f"movie/{self.movie_id}", append_to_response=append_to_response, include_image_language=image_language)
        return utils.as_dataclass(schemas.Movie, data)

    async def alternative_titles(self, *, country: Optional[str] = None) -> schemas.AlternativeTitles:
        """Get all of the alternative titles for a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-alternative-titles
        """
        data = await self.request(f"movie/{self.movie_id}/alternative_titles", country=country)
        return utils.as_dataclass(schemas.AlternativeTitles, data)

    async def credits(self) -> schemas.Credits:
        """Get the cast and crew for a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-credits
        """
        data = await self.request(f"movie/{self.movie_id}/credits")
        return utils.as_dataclass(schemas.Credits, data)

    async def external_ids(self) -> schemas.ExternalIDs:
        """Get the external ids for a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-external-ids
        """
        data = await self.request(f"movie/{self.movie_id}/external_ids")
        return utils.as_dataclass(schemas.ExternalIDs, data)

    async def keywords(self) -> schemas.Keywords:
        """Get the keywords that have been added to a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-keywords
        """
        data = await self.request(f"movie/{self.movie_id}/keywords")
        return utils.as_dataclass(schemas.Keywords, data)

    async def images(self, *, include_image_language: Optional[str] = None) -> schemas.Images:
        """Get the images that belong to a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-images
        """
        data = await self.request(f"movie/{self.movie_id}/images", include_image_language=include_image_language)
        return utils.as_dataclass(schemas.Images, data)

    async def lists(self, *, page: int = 1) -> schemas.ItemsList:
        """Get a list of lists that this movie belongs to.

        See more: https://developers.themoviedb.org/3/movies/get-movie-lists
        """
        data = await self.request(f"movie/{self.movie_id}/lists", page=page)
        return utils.as_dataclass(schemas.ItemsList, data)

    async def recommendations(self, *, page: int = 1) -> schemas.Movies:
        """Get a list of recommended movies for a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-recommendations
        """
        data = await self.request(f"movie/{self.movie_id}/recommendations", page=page)
        return utils.as_dataclass(schemas.Movies, data)

    async def release_dates(self) -> schemas.ReleaseDates:
        """Get the release date along with the certification for a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-release-dates
        """
        data = await self.request(f"movie/{self.movie_id}/release_dates")
        return utils.as_dataclass(schemas.ReleaseDates, data)

    async def reviews(self, *, page: int = 1) -> schemas.Reviews:
        """Get the user reviews for a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-reviews
        """
        data = await self.request(f"movie/{self.movie_id}/reviews", page=page)
        return utils.as_dataclass(schemas.Reviews, data)

    async def similar(self, *, page: int = 1) -> schemas.Movies:
        """Get a list of similar movies.

        See more: https://developers.themoviedb.org/3/movies/get-similar-movies
        """
        data = await self.request(f"movie/{self.movie_id}/similar", page=page)
        return utils.as_dataclass(schemas.Movies, data)

    async def translations(self) -> schemas.Translations:
        """Get a list of translations that have been created for a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-translations
        """
        data = await self.request(f"movie/{self.movie_id}/translations")
        return utils.as_dataclass(schemas.Translations, data)

    async def videos(self, *, page: int = 1) -> schemas.Videos:
        """Get the videos that have been added to a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-videos
        """
        data = await self.request(f"movie/{self.movie_id}/videos", page=page)
        return utils.as_dataclass(schemas.Videos, data)

    async def watch_providers(self) -> schemas.WatchProviders:
        """Get a list of the availabilities per country by provider.

        See more: https://developers.themoviedb.org/3/movies/get-movie-watch-providers
        """
        data = await self.request(f"movie/{self.movie_id}/watch/providers")
        return utils.as_dataclass(schemas.WatchProviders, data)


class Movies(Base):

    async def latest(self) -> schemas.Movie:
        """Get the most newly created movie.

        See more: https://developers.themoviedb.org/3/movies/get-latest-movie
        """
        data = await self.request("movie/latest")
        return utils.as_dataclass(schemas.Movie, data)

    async def now_playing(self, *, page: int = 1) -> schemas.Movies:
        """Get a list of movies in theatres.

        See more: https://developers.themoviedb.org/3/movies/get-now-playing
        """
        data = await self.request("movie/now_playing", page=page)
        return utils.as_dataclass(schemas.Movies, data)

    async def popular(self, *, page: int = 1) -> schemas.Movies:
        """Get a list of the current popular movies on TMDB.

        See more: https://developers.themoviedb.org/3/movies/get-popular-movies
        """
        data = await self.request("movie/popular", page=page)
        return utils.as_dataclass(schemas.Movies, data)

    async def top_rated(self, *, page: int = 1) -> schemas.Movies:
        """Get the top rated movies on TMDB.

        See more: https://developers.themoviedb.org/3/movies/get-top-rated-movies
        """
        data = await self.request("movie/top_rated", page=page)
        return utils.as_dataclass(schemas.Movies, data)

    async def upcoming(self, *, page: int = 1) -> schemas.Movies:
        """Get a list of upcoming movies in theatres.

        See more: https://developers.themoviedb.org/3/movies/get-upcoming
        """
        data = await self.request("movie/upcoming", page=page)
        return utils.as_dataclass(schemas.Movies, data)
