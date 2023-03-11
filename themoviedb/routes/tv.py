# -*- coding: utf-8 -*-
from themoviedb import schemas, utils
from themoviedb.routes.base import Base


class TV(Base):
    def __init__(self, tv_id: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.tv_id = tv_id

    async def details(self, *, append_to_response: str = None) -> schemas.TV:
        """Get the primary TV show details by id.

        See more: https://developers.themoviedb.org/3/tv/get-tv-details
        """
        data = await self.request(f"tv/{self.tv_id}", append_to_response=append_to_response)
        return utils.as_dataclass(schemas.TV, data)

    async def aggregate_credits(self) -> schemas.Credits:
        """Get the credits (cast and crew) that have been added to a TV show.

        This call differs from the main credits call in that it does
        not return the newest season but rather, is a view of all the
        entire cast & crew for all episodes belonging to a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-aggregate-credits
        """
        data = await self.request(f"tv/{self.tv_id}/aggregate_credits")
        return utils.as_dataclass(schemas.Credits, data)

    async def alternative_titles(self, *, country: str = None) -> schemas.AlternativeTitles:
        """Get all alternative titles for a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-alternative-titles
        """
        data = await self.request(f"tv/{self.tv_id}/alternative_titles", country=country)
        return utils.as_dataclass(schemas.AlternativeTitles, data)

    async def credits(self) -> schemas.Credits:
        """Get the credits (cast and crew) that have been added to a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-credits
        """
        data = await self.request(f"tv/{self.tv_id}/credits")
        return utils.as_dataclass(schemas.Credits, data)

    async def external_ids(self) -> schemas.ExternalIDs:
        """Get the external ids for a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-external-ids
        """
        data = await self.request(f"tv/{self.tv_id}/external_ids")
        return utils.as_dataclass(schemas.ExternalIDs, data)

    async def images(self) -> schemas.Images:
        """Get the images that belong to a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-images
        """
        data = await self.request(f"tv/{self.tv_id}/images")
        return utils.as_dataclass(schemas.Images, data)

    async def keywords(self) -> schemas.Keywords:
        """Get the keywords that have been added to a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-keywords
        """
        data = await self.request(f"tv/{self.tv_id}/keywords")
        return utils.as_dataclass(schemas.Keywords, data)

    async def recommendations(self, *, page: int = 1) -> schemas.TVs:
        """Get the list of TV show recommendations for this item.

        See more: https://developers.themoviedb.org/3/tv/get-tv-recommendations
        """
        data = await self.request(f"tv/{self.tv_id}/recommendations", page=page)
        return utils.as_dataclass(schemas.TVs, data)

    async def reviews(self, *, page: int = 1) -> schemas.Reviews:
        """Get the reviews for a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-reviews
        """
        data = await self.request(f"tv/{self.tv_id}/reviews", page=page)
        return utils.as_dataclass(schemas.Reviews, data)

    async def screened_theatrically(self, *, page: int = 1) -> schemas.Episodes:
        """Get a list of seasons or episodes that have been screened in a film festival or theatre.

        See more: https://developers.themoviedb.org/3/tv/get-screened-theatrically
        """
        data = await self.request(f"tv/{self.tv_id}/screened_theatrically")
        return utils.as_dataclass(schemas.Episodes, data)

    async def similar(self, *, page: int = 1) -> schemas.TVs:
        """Get a list of similar TV shows. These items are assembled by looking at keywords and genres.

        See more: https://developers.themoviedb.org/3/tv/get-similar-tv-shows
        """
        data = await self.request(f"tv/{self.tv_id}/similar", page=page)
        return utils.as_dataclass(schemas.TVs, data)

    async def translations(self) -> schemas.Translations:
        """Get a list of the translations that exist for a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-translations
        """
        data = await self.request(f"tv/{self.tv_id}/translations")
        return utils.as_dataclass(schemas.Translations, data)

    async def videos(self, *, page: int = 1) -> schemas.Videos:
        """Get the videos that have been added to a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-videos
        """
        data = await self.request(f"tv/{self.tv_id}/videos", page=page)
        return utils.as_dataclass(schemas.Videos, data)

    async def watch_providers(self) -> schemas.WatchProviders:
        """Get a list of the availabilities per country by provider.

        See more: https://developers.themoviedb.org/3/tv/get-tv-watch-providers
        """
        data = await self.request(f"tv/{self.tv_id}/watch/providers")
        return utils.as_dataclass(schemas.WatchProviders, data)


class TVs(Base):

    async def latest(self) -> schemas.TV:
        """Get the most newly created TV show.

        See more: https://developers.themoviedb.org/3/tv/get-latest-tv
        """
        data = await self.request("tv/latest")
        return utils.as_dataclass(schemas.TV, data)

    async def airing_today(self, *, page: int = 1) -> schemas.TVs:
        """Get a list of TV shows that are airing today.

        See more: https://developers.themoviedb.org/3/tv/get-tv-airing-today
        """
        data = await self.request("tv/airing_today", page=page)
        return utils.as_dataclass(schemas.TVs, data)

    async def on_the_air(self, *, page: int = 1) -> schemas.TVs:
        """Get a list of shows that are currently on the air.

        See more: https://developers.themoviedb.org/3/tv/get-tv-on-the-air
        """
        data = await self.request("tv/on_the_air", page=page)
        return utils.as_dataclass(schemas.TVs, data)

    async def popular(self, *, page: int = 1) -> schemas.TVs:
        """Get a list of the current popular TV shows on TMDB.

        See more: https://developers.themoviedb.org/3/tv/get-popular-tv-shows
        """
        data = await self.request("tv/popular", page=page)
        return utils.as_dataclass(schemas.TVs, data)

    async def top_rated(self, *, page: int = 1) -> schemas.TVs:
        """Get a list of the top rated TV shows on TMDB.

        See more: https://developers.themoviedb.org/3/tv/get-top-rated-tv
        """
        data = await self.request("tv/top_rated", page=page)
        return utils.as_dataclass(schemas.TVs, data)
