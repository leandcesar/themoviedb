from typing import Optional

from themoviedb import schemas, utils
from themoviedb.routes_async._base import Base


class Episode(Base):
    def __init__(self, tv_id: int, season_id: int, episode_id: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.tv_id = tv_id
        self.season_id = season_id
        self.episode_id = episode_id

    async def details(self, *, append_to_response: Optional[str] = None) -> schemas.Episode:
        """Get the TV season details by id.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-details
        """
        data = await self.request(f"tv/{self.tv_id}/season/{self.season_id}/episode/{self.episode_id}", append_to_response=append_to_response)
        return utils.as_dataclass(schemas.Episode, data)

    async def credits(self) -> schemas.Credits:
        """Get the credits for TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-credits
        """
        data = await self.request(f"tv/{self.tv_id}/season/{self.season_id}/episode/{self.episode_id}/credits")
        return utils.as_dataclass(schemas.Credits, data)

    async def external_ids(self) -> schemas.ExternalIDs:
        """Get the external ids for a TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-external-ids
        """
        data = await self.request(f"tv/{self.tv_id}/season/{self.season_id}/episode/{self.episode_id}/external_ids")
        return utils.as_dataclass(schemas.ExternalIDs, data)

    async def images(self) -> schemas.Images:
        """Get the images that belong to a TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-images
        """
        data = await self.request(f"tv/{self.tv_id}/season/{self.season_id}/episode/{self.episode_id}/images")
        return utils.as_dataclass(schemas.Images, data)

    async def translations(self) -> schemas.Translations:
        """Get the credits for TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-translations
        """
        data = await self.request(f"tv/{self.tv_id}/season/{self.season_id}/episode/{self.episode_id}/translations")
        return utils.as_dataclass(schemas.Translations, data)

    async def videos(self) -> schemas.Videos:
        """Get the videos that have been added to a TV season.

        See more: https://developers.themoviedb.org/3/tv-seasons/get-tv-season-videos
        """
        data = await self.request(f"tv/{self.tv_id}/season/{self.season_id}/episode/{self.episode_id}/videos")
        return utils.as_dataclass(schemas.Videos, data)
