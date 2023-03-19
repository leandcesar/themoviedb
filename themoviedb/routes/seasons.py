from typing import Optional

from themoviedb import schemas, utils
from themoviedb.routes._base import Base


class Season(Base):
    def __init__(self, tv_id: int, season_id: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.tv_id = tv_id
        self.season_id = season_id

    async def details(self, *, append_to_response: Optional[str] = None) -> schemas.Season:
        """Get the TV season details by id.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-details
        """
        data = await self.request(f"tv/{self.tv_id}/season/{self.season_id}", append_to_response=append_to_response)
        return utils.as_dataclass(schemas.Season, data)

    async def aggregate_credits(self) -> schemas.Credits:
        """Get the aggregate credits for TV season.

        This call differs from the main credits call in that it does
        not return the newest season but rather, is a view of all the
        entire cast & crew for all episodes belonging to a TV show.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-aggregate-credits
        """
        data = await self.request(f"tv/{self.tv_id}/season/{self.season_id}/aggregate_credits")
        return utils.as_dataclass(schemas.Credits, data)

    async def credits(self) -> schemas.Credits:
        """Get the credits for TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-credits
        """
        data = await self.request(f"tv/{self.tv_id}/season/{self.season_id}/credits")
        return utils.as_dataclass(schemas.Credits, data)

    async def external_ids(self) -> schemas.ExternalIDs:
        """Get the external ids for a TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-external-ids
        """
        data = await self.request(f"tv/{self.tv_id}/season/{self.season_id}/external_ids")
        return utils.as_dataclass(schemas.ExternalIDs, data)

    async def images(self) -> schemas.Images:
        """Get the images that belong to a TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-images
        """
        data = await self.request(f"tv/{self.tv_id}/season/{self.season_id}/images")
        return utils.as_dataclass(schemas.Images, data)

    async def translations(self) -> schemas.Translations:
        """Get the credits for TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-translations
        """
        data = await self.request(f"tv/{self.tv_id}/season/{self.season_id}/translations")
        return utils.as_dataclass(schemas.Translations, data)

    async def videos(self) -> schemas.Videos:
        """Get the videos that have been added to a TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-videos
        """
        data = await self.request(f"tv/{self.tv_id}/season/{self.season_id}/videos")
        return utils.as_dataclass(schemas.Videos, data)
