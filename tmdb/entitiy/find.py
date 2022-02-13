# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional

from .media import Media
from .person import PersonPartial


@dataclass
class Find:
    movie_results: Optional[list[Media]]
    person_results: Optional[list[PersonPartial]]
    tv_episode_results: Optional[list[Media]]
    tv_results: Optional[list[Media]]
    tv_season_results: Optional[list[Media]]

    def __bool__(self) -> bool:
        return (
            self.movie_results
            or self.person_results
            or self.tv_episode_results
            or self.tv_results
            or self.tv_season_results
        )
