# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import List, Optional

from themoviedb.schemas._enums import MediaType
from themoviedb.schemas._partial import (
    PartialEpisode,
    PartialMovie,
    PartialPerson,
    PartialSeason,
    PartialTV,
)
from themoviedb.schemas._result import ResultWithPage


@dataclass
class Multi(PartialMovie, PartialPerson, PartialTV):
    def __str__(self) -> str:
        return self.name or self.title or self.original_name or self.original_title or ""

    def is_movie(self) -> bool:
        return self.media_type == MediaType.movie

    def is_person(self) -> bool:
        return self.media_type == MediaType.person

    def is_tv(self) -> bool:
        return self.media_type == MediaType.tv


@dataclass
class Multis(ResultWithPage):
    results: Optional[List[Multi]] = None


@dataclass
class MultiResults:
    movie_results: Optional[List[PartialMovie]] = None
    person_results: Optional[List[PartialPerson]] = None
    tv_results: Optional[List[PartialTV]] = None
    tv_episode_results: Optional[List[PartialEpisode]] = None
    tv_season_results: Optional[List[PartialSeason]] = None
