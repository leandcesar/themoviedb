# -*- coding: utf-8 -*-
from .base import Base, Response


class Show(Base):
    async def details(self, tv_id: int, *, append: str = None, image_language: str = "null") -> Response:
        """Get the primary TV show details by id.

        See more: https://developers.themoviedb.org/3/tv/get-tv-details
        """
        return await self.request(f"tv/{tv_id}", append_to_response=append, include_image_language=image_language)

    async def aggregate_credits(self, tv_id: int) -> Response:
        """Get the aggregate credits (cast and crew) that have been added to a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-aggregate-credits
        """
        return await self.request(f"tv/{tv_id}/aggregate_credits")

    async def airing_today(self, *, page: int = 1) -> Response:
        """Get a list of TV shows that are airing today.

        See more: https://developers.themoviedb.org/3/tv/get-tv-airing-today
        """
        return await self.request("tv/airing_today", page=page)

    async def alternative_titles(self, tv_id: int) -> Response:
        """Get all of the alternative titles for a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-alternative-titles
        """
        return await self.request(f"tv/{tv_id}/alternative_titles")

    async def certifications(self) -> Response:
        """Get an up to date list of the officially supported TV show certifications on TMDB.

        See more: https://developers.themoviedb.org/3/certifications/get-tv-certifications
        """
        return await self.request("certification/tv/list")

    async def changes(self, tv_id: int, *, start_date: str = None, end_date: str = None, page: int = 1) -> Response:
        """Get the changes for a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-changes
        """
        return await self.request(f"tv/{tv_id}/changes", start_date=start_date, end_date=end_date, page=page)

    async def content_ratings(self, tv_id: int) -> Response:
        """Get the list of content ratings (certifications) that have been added to a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-content-ratings
        """
        return await self.request(f"tv/{tv_id}/content_ratings")

    async def credits(self, tv_id: int) -> Response:
        """Get the credits (cast and crew) that have been added to a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-credits
        """
        return await self.request(f"tv/{tv_id}/credits")

    async def discover(
        self,
        *,
        page: int = 1,
        sort_by: str = "popularity.desc",
        air_date__gte: str = None,
        air_date__lte: str = None,
        first_air_date__gte: str = None,
        first_air_date__lte: str = None,
        first_air_date_year: int = None,
        timezone: str = None,
        vote_average__gte: float = None,
        vote_count__gte: int = None,
        with_genres: str = None,
        with_networks: str = None,
        without_genres: str = None,
        with_runtime__gte: int = None,
        with_runtime__lte: int = None,
        include_null_first_air_dates: bool = None,
        with_original_language: str = None,
        without_keywords: str = None,
        screened_theatrically: bool = None,
        with_companies: str = None,
        with_keywords: str = None,
        with_watch_providers: str = None,
        watch_region: str = None,
        with_watch_monetization_types: str = None,
    ) -> Response:
        """Discover TV shows by different types of data.

        See more: https://developers.themoviedb.org/3/discover/tv-discover
        """
        return await self.request(
            "discover/tv",
            page=page,
            sort_by=sort_by,
            watch_region=watch_region,
            air_date__gte=air_date__gte,
            air_date__lte=air_date__lte,
            first_air_date__gte=first_air_date__gte,
            first_air_date__lte=first_air_date__lte,
            first_air_date_year=first_air_date_year,
            timezone=timezone,
            vote_average__gte=vote_average__gte,
            vote_count__gte=vote_count__gte,
            with_genres=with_genres,
            with_networks=with_networks,
            without_genres=without_genres,
            with_runtime__gte=with_runtime__gte,
            with_runtime__lte=with_runtime__lte,
            include_null_first_air_dates=include_null_first_air_dates,
            with_original_language=with_original_language,
            without_keywords=without_keywords,
            screened_theatrically=screened_theatrically,
            with_companies=with_companies,
            with_keywords=with_keywords,
            with_watch_providers=with_watch_providers,
            with_watch_monetization_types=with_watch_monetization_types,
        )

    async def episode_groups(self, tv_id: int) -> Response:
        """Get all of the episode groups that have been created for a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-episode-groups
        """
        return await self.request(f"tv/{tv_id}/episode_groups")

    async def external_ids(self, tv_id: int) -> Response:
        """Get the external ids for a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-external-ids
        """
        return await self.request(f"tv/{tv_id}/external_ids")

    async def genres(self) -> Response:
        """Get the list of official genres for TV shows.

        See more: https://developers.themoviedb.org/3/genres/get-tv-list
        """
        return await self.request("genre/tv/list")

    async def images(self, tv_id: int) -> Response:
        """Get the images that belong to a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-images
        """
        return await self.request(f"tv/{tv_id}/images")

    async def keywords(self, tv_id: int) -> Response:
        """Get the keywords that have been added to a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-keywords
        """
        return await self.request(f"tv/{tv_id}/keywords")

    async def latest(self) -> Response:
        """Get the most newly created TV show.

        See more: https://developers.themoviedb.org/3/tv/get-latest-tv
        """
        return await self.request("tv/latest")

    async def on_the_air(self, *, page: int = 1) -> Response:
        """Get a list of TV shows that are airing today.

        See more: https://developers.themoviedb.org/3/tv/get-tv-on-the-air
        """
        return await self.request("tv/on_the_air", page=page)

    async def popular(self, *, page: int = 1) -> Response:
        """Get a list of the current popular TV shows on TMDB.

        See more: https://developers.themoviedb.org/3/tv/get-popular-tv-shows
        """
        return await self.request("tv/popular", page=page)

    async def providers(self, tv_id: int) -> Response:
        """Get a list of the availabilities per country by provider.

        See more: https://developers.themoviedb.org/3/tv/get-tv-watch-providers
        """
        return await self.request(f"tv/{tv_id}/watch/providers")

    async def providers_list(self, *, watch_region=None) -> Response:
        """Returns a list of the watch provider (OTT/streaming) data we have available for TV series.

        See more: https://developers.themoviedb.org/3/watch-providers/get-tv-providers
        """
        return await self.request("watch/providers/tv", watch_region=watch_region)

    async def recommendations(self, tv_id: int, *, page: int = 1) -> Response:
        """Get the list of TV show recommendations for this item.

        See more: https://developers.themoviedb.org/3/tv/get-tv-recommendations
        """
        return await self.request(f"tv/{tv_id}/recommendations", page=page)

    async def reviews(self, tv_id: int, *, page: int = 1) -> Response:
        """Get the reviews for a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-reviews
        """
        return await self.request(f"tv/{tv_id}/reviews", page=page)

    async def screened_theatrically(self, tv_id: int) -> Response:
        """Get a list of seasons or episodes that have been screened in a film festival or theatre.

        See more: https://developers.themoviedb.org/3/tv/get-screened-theatrically
        """
        return await self.request(f"tv/{tv_id}/screened_theatrically")

    async def search(
        self,
        query: str,
        *,
        page: int = 1,
        include_adult: bool = False,
        first_air_date_year: int = None,
    ) -> Response:
        """Search for a TV show.

        See more: https://developers.themoviedb.org/3/search/search-tv-shows
        """
        return await self.request(
            "search/tv",
            query=query,
            page=page,
            include_adult=include_adult,
            first_air_date_year=first_air_date_year,
        )

    async def similar(self, tv_id: int, *, page: int = 1) -> Response:
        """Get a list of similar TV shows.

        See more: https://developers.themoviedb.org/3/tv/get-similar-tv-shows
        """
        return await self.request(f"tv/{tv_id}/similar", page=page)

    async def top_rated(self, *, page: int = 1) -> Response:
        """Get a list of the top rated TV shows on TMDB.

        See more: https://developers.themoviedb.org/3/tv/get-top-rated-tv
        """
        return await self.request("tv/top_rated", page=page)

    async def translations(self, tv_id: int) -> Response:
        """Get a list of the translations that exist for a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-translations
        """
        return await self.request(f"tv/{tv_id}/translations")

    async def trending(self, *, interval: str = "day", page: int = 1) -> Response:
        """Get the daily (`interval=day`) or weekly (`interval=week`) trending TV shows.

        See more: https://developers.themoviedb.org/3/trending/get-trending
        """
        return await self.request(f"trending/tv/{interval}", page=page)

    async def videos(self, tv_id: int) -> Response:
        """Get the videos that have been added to a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-videos
        """
        return await self.request(f"tv/{tv_id}/videos")
