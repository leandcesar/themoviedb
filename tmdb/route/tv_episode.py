# -*- coding: utf-8 -*-
from .base import Base, Response


class Episode(Base):
    async def details(
        self,
        tv_id: int,
        season_number: int,
        episode_number: int,
        *,
        append_to_response: str = None,
    ) -> Response:
        """Get the TV episode details by id.

        See more: https://developers.themoviedb.org/3/tv-episodes/get-tv-episode-details
        """
        return await self.request(f"tv/{tv_id}/season/{season_number}/episode/{episode_number}", append_to_response=append_to_response)

    async def changes(self, tv_id: int, season_number: int, episode_number: int, *, start_date: str = None, end_date: str = None, page: int = 1) -> Response:
        """Get the changes for a TV episode.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-changes
        """
        return await self.request(f"tv/{tv_id}/season/{season_number}/episode/{episode_number}/changes", start_date=start_date, end_date=end_date, page=page)

    async def credits(self, tv_id: int, season_number: int, episode_number: int) -> Response:
        """Get the credits (cast, crew and guest stars) for a TV episode.

        See more: https://developers.themoviedb.org/3/tv-episodes/get-tv-episode-credits
        """
        return await self.request(f"tv/{tv_id}/season/{season_number}/episode/{episode_number}/credits")

    async def external_ids(self, tv_id: int, season_number: int, episode_number: int) -> Response:
        """Get the external ids for a TV episode.

        See more: https://developers.themoviedb.org/3/tv-episodes/get-tv-episode-external-ids
        """
        return await self.request(f"tv/{tv_id}/season/{season_number}/episode/{episode_number}/external_ids")

    async def images(self, tv_id: int, season_number: int, episode_number: int) -> Response:
        """Get the images that belong to a TV episode.

        See more: https://developers.themoviedb.org/3/tv-episodes/get-tv-episode-images
        """
        return await self.request(f"tv/{tv_id}/season/{season_number}/episode/{episode_number}/images")

    async def translations(self, tv_id: int, season_number: int, episode_number: int) -> Response:
        """Get the translation data for an episode.

        See more: https://developers.themoviedb.org/3/tv-episodes/get-tv-episode-translations
        """
        return await self.request(f"tv/{tv_id}/season/{season_number}/episode/{episode_number}/translations")

    async def videos(self, tv_id: int, season_number: int, episode_number: int) -> Response:
        """Get the videos that have been added to a TV episode.

        See more: https://developers.themoviedb.org/3/tv-episodes/get-tv-episode-videos
        """
        return await self.request(f"tv/{tv_id}/season/{season_number}/episode/{episode_number}/videos")
