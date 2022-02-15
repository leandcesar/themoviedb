# -*- coding: utf-8 -*-
from .base import Base, Response


class Movie(Base):
    async def details(self, movie_id: int, *, append: str = None, image_language: str = "null") -> Response:
        """Get the primary information about a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-details
        """
        return await self.request(f"movie/{movie_id}", append_to_response=append, include_image_language=image_language)

    async def alternative_titles(self, movie_id: int, *, country: str = None) -> Response:
        """Get all of the alternative titles for a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-alternative-titles
        """
        return await self.request(f"movie/{movie_id}/alternative_titles", country=country)

    async def certifications(self) -> Response:
        """Get an up to date list of the officially supported movie certifications on TMDB.

        See more: https://developers.themoviedb.org/3/certifications/get-movie-certifications
        """
        return await self.request("certification/movie/list")

    async def changes(self, movie_id: int, *, start_date: str = None, end_date: str = None, page: int = 1) -> Response:
        """Get the changes for a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-changes
        """
        return await self.request(f"movie/{movie_id}/changes", start_date=start_date, end_date=end_date, page=page)

    async def credits(self, movie_id: int) -> Response:
        """Get the cast and crew for a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-credits
        """
        return await self.request(f"movie/{movie_id}/credits")

    async def discover(
        self,
        *,
        page: int = 1,
        sort_by: str = "popularity.desc",
        certification_country: str = None,
        certification: str = None,
        certification__lte: str = None,
        certification__gte: str = None,
        include_adult: bool = None,
        include_video: bool = None,
        primary_release_year: int = None,
        primary_release_date__gte: str = None,
        primary_release_date__lte: str = None,
        release_date__gte: str = None,
        release_date__lte: str = None,
        with_release_type: int = None,
        year: int = None,
        vote_count__gte: int = None,
        vote_count__lte: int = None,
        vote_average__gte: float = None,
        vote_average__lte: float = None,
        with_cast: str = None,
        with_crew: str = None,
        with_people: str = None,
        with_companies: str = None,
        with_genres: str = None,
        without_genres: str = None,
        with_keywords: str = None,
        without_keywords: str = None,
        with_runtime__gte: int = None,
        with_runtime__lte: int = None,
        with_original_language: str = None,
        with_watch_providers: str = None,
        watch_region: str = None,
        with_watch_monetization_types: str = None,
    ) -> Response:
        """Discover movies by different types of data.

        See more: https://developers.themoviedb.org/3/discover/movie-discover
        """
        return await self.request(
            "discover/movie",
            page=page,
            sort_by=sort_by,
            watch_region=watch_region,
            certification_country=certification_country,
            certification=certification,
            certification__lte=certification__lte,
            certification__gte=certification__gte,
            include_adult=include_adult,
            include_video=include_video,
            primary_release_year=primary_release_year,
            primary_release_date__gte=primary_release_date__gte,
            primary_release_date__lte=primary_release_date__lte,
            release_date__gte=release_date__gte,
            release_date__lte=release_date__lte,
            with_release_type=with_release_type,
            year=year,
            vote_count__gte=vote_count__gte,
            vote_count__lte=vote_count__lte,
            vote_average__gte=vote_average__gte,
            vote_average__lte=vote_average__lte,
            with_cast=with_cast,
            with_crew=with_crew,
            with_people=with_people,
            with_companies=with_companies,
            with_genres=with_genres,
            without_genres=without_genres,
            with_keywords=with_keywords,
            without_keywords=without_keywords,
            with_runtime__gte=with_runtime__gte,
            with_runtime__lte=with_runtime__lte,
            with_original_language=with_original_language,
            with_watch_providers=with_watch_providers,
            with_watch_monetization_types=with_watch_monetization_types,
        )

    async def external_ids(self, movie_id: int) -> Response:
        """Get the external ids for a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-external-ids
        """
        return await self.request(f"movie/{movie_id}/external_ids")

    async def genres(self) -> Response:
        """Get the list of official genres for movies.

        See more: https://developers.themoviedb.org/3/genres/get-movie-list
        """
        return await self.request("genre/movie/list")

    async def keywords(self, movie_id: int) -> Response:
        """Get the keywords that have been added to a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-keywords
        """
        return await self.request(f"movie/{movie_id}/keywords")

    async def images(self, movie_id: int, *, include_image_language: str = None) -> Response:
        """Get the images that belong to a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-images
        """
        return await self.request(f"movie/{movie_id}/images", include_image_language=include_image_language)

    async def latest(self) -> Response:
        """Get the most newly created movie.

        See more: https://developers.themoviedb.org/3/movies/get-latest-movie
        """
        return await self.request("movie/latest")

    async def lists(self, movie_id: int, *, page: int = 1) -> Response:
        """Get a list of lists that this movie belongs to.

        See more: https://developers.themoviedb.org/3/movies/get-movie-lists
        """
        return await self.request(f"movie/{movie_id}/lists", page=page)

    async def now_playing(self, *, page: int = 1) -> Response:
        """Get a list of movies in theatres.

        See more: https://developers.themoviedb.org/3/movies/get-now-playing
        """
        return await self.request("movie/now_playing", page=page)

    async def popular(self, *, page: int = 1) -> Response:
        """Get a list of the current popular movies on TMDB.

        See more: https://developers.themoviedb.org/3/movies/get-popular-movies
        """
        return await self.request("movie/popular", page=page)

    async def providers(self, movie_id: int) -> Response:
        """Get a list of the availabilities per country by provider.

        See more: https://developers.themoviedb.org/3/movies/get-movie-watch-providers
        """
        return await self.request(f"movie/{movie_id}/watch/providers")

    async def providers_list(self) -> Response:
        """Returns a list of the watch provider (OTT/streaming) data we have available for movies.

        See more: https://developers.themoviedb.org/3/watch-providers/get-movie-providers
        """
        return await self.request("watch/providers/movie", watch_region=self.region)

    async def recommendations(self, movie_id: int, *, page: int = 1) -> Response:
        """Get a list of recommended movies for a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-recommendations
        """
        return await self.request(f"movie/{movie_id}/recommendations", page=page)

    async def release_dates(self, movie_id: int, *, page: int = 1) -> Response:
        """Get the release date along with the certification for a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-release-dates
        """
        return await self.request(f"movie/{movie_id}/release_dates", page=page)

    async def reviews(self, movie_id: int, *, page: int = 1) -> Response:
        """Get the user reviews for a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-reviews
        """
        return await self.request(f"movie/{movie_id}/reviews", page=page)

    async def search(
        self,
        query: str,
        *,
        page: int = 1,
        include_adult: bool = False,
        year: int = None,
        primary_release_year: int = None,
    ) -> Response:
        """Search for movies.

        See more: https://developers.themoviedb.org/3/search/search-movies
        """
        return await self.request(
            "search/movie",
            query=query,
            page=page,
            include_adult=include_adult,
            year=year,
            primary_release_year=primary_release_year,
        )

    async def similar(self, movie_id: int, *, page: int = 1) -> Response:
        """Get a list of similar movies.

        See more: https://developers.themoviedb.org/3/movies/get-similar-movies
        """
        return await self.request(f"movie/{movie_id}/similar", page=page)

    async def top_rated(self, *, page: int = 1) -> Response:
        """Get the top rated movies on TMDB.

        See more: https://developers.themoviedb.org/3/movies/get-top-rated-movies
        """
        return await self.request("movie/top_rated", page=page)

    async def translations(self, movie_id: int) -> Response:
        """Get a list of translations that have been created for a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-translations
        """
        return await self.request(f"movie/{movie_id}/translations")

    async def trending(self, *, interval: str = "day", page: int = 1) -> Response:
        """Get the daily (`interval=day`) or weekly (`interval=week`) trending movies.

        See more: https://developers.themoviedb.org/3/trending/get-trending
        """
        return await self.request(f"trending/movie/{interval}", page=page)

    async def upcoming(self, *, page: int = 1) -> Response:
        """Get a list of upcoming movies in theatres.

        See more: https://developers.themoviedb.org/3/movies/get-upcoming
        """
        return await self.request("movie/upcoming", page=page)

    async def videos(self, movie_id: int, *, page: int = 1) -> Response:
        """Get the videos that have been added to a movie.

        See more: https://developers.themoviedb.org/3/movies/get-movie-videos
        """
        return await self.request(f"movie/{movie_id}/videos", page=page)
