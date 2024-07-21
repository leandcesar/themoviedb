# -*- coding: utf-8 -*-
from typing import Optional

from themoviedb import schemas, utils
from themoviedb.routes_sync._base import Base


class Guest(Base):
    def __init__(self, guest_session_id: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.guest_session_id = guest_session_id

    def rated_movies(self, *, sort_by: Optional[str] = None) -> schemas.RatedMovies:
        """Get the rated movies for a guest session.

        See more: https://developers.themoviedb.org/3/guest-sessions/get-guest-session-rated-movies
        """
        data = self.request(f"guest_session/{self.guest_session_id}/rated/movies")
        return utils.as_dataclass(schemas.RatedMovies, data)

    def rated_tvs(self, *, sort_by: Optional[str] = None) -> schemas.RatedTVs:
        """Get the rated TV shows for a guest session.

        See more: https://developers.themoviedb.org/3/guest-sessions/get-guest-session-rated-tv-shows
        """
        data = self.request(f"guest_session/{self.guest_session_id}/rated/tv")
        return utils.as_dataclass(schemas.RatedTVs, data)

    def rated_episodes(self, *, sort_by: Optional[str] = None) -> schemas.RatedEpisodes:
        """Get the rated TV episodes for a guest session.

        See more: https://developers.themoviedb.org/3/guest-sessions/get-gest-session-rated-tv-episodes
        """
        data = self.request(f"guest_session/{self.guest_session_id}/rated/episodes")
        return utils.as_dataclass(schemas.RatedEpisodes, data)
