# -*- coding: utf-8 -*-
from .base import Base, Response


class Season(Base):
    async def details(
        self,
        tv_id: int,
        season_number: int,
        *,
        append_to_response: str = None,
    ) -> Response:
        """Get the TV season details by id.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-details
        """
        return await self.request(f"tv/{tv_id}/season/{season_number}", append_to_response=append_to_response)

    async def aggregate_credits(self, tv_id: int, season_number: int) -> Response:
        """Get the aggregate credits for TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-aggregate-credits
        """
        return await self.request(f"tv/{tv_id}/season/{season_number}/aggregate_credits")

    async def alternative_titles(self, tv_id: int, season_number: int) -> Response:
        """Get all of the alternative titles for a TV show.

        See more: https://developers.themoviedb.org/3/tv/get-tv-alternative-titles
        """
        return await self.request(f"tv/{tv_id}/season/{season_number}/alternative_titles")

    async def changes(self, tv_id: int, season_number: int, *, start_date: str = None, end_date: str = None, page: int = 1) -> Response:
        """Get the changes for a TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-changes
        """
        return await self.request(f"tv/{tv_id}/season/{season_number}/changes", start_date=start_date, end_date=end_date, page=page)

    async def credits(self, tv_id: int, season_number: int) -> Response:
        """Get the credits for TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-credits
        """
        return await self.request(f"tv/{tv_id}/season/{season_number}/credits")

    async def external_ids(self, tv_id: int, season_number: int) -> Response:
        """Get the external ids for a TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-external-ids
        """
        return await self.request(f"tv/{tv_id}/season/{season_number}/external_ids")

    async def images(self, tv_id: int, season_number: int) -> Response:
        """Get the images that belong to a TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-images
        """
        return await self.request(f"tv/{tv_id}/season/{season_number}/images")

    async def translations(self, tv_id: int, season_number: int) -> Response:
        """Get the credits for TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-translations
        """
        return await self.request(f"tv/{tv_id}/season/{season_number}/translations")

    async def videos(self, tv_id: int, season_number: int) -> Response:
        """Get the videos that have been added to a TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-videos
        """
        return await self.request(f"tv/{tv_id}/season/{season_number}/videos")
