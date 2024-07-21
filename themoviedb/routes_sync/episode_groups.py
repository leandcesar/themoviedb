# -*- coding: utf-8 -*-
from themoviedb import schemas, utils
from themoviedb.routes_sync._base import Base


class EpisodeGroup(Base):
    def __init__(self, episode_group_id: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.episode_group_id = episode_group_id

    def details(self) -> schemas.EpisodeGroup:
        """Get the details of a TV episode group.

        See more: https://developers.themoviedb.org/3/tv-episode-groups/get-tv-episode-group-details
        """
        data = self.request(f"tv/episode_group/{self.episode_group_id}")
        return utils.as_dataclass(schemas.EpisodeGroup, data)
