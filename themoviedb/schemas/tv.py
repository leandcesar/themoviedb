from dataclasses import dataclass
from datetime import date
from typing import List, Optional, Union

from themoviedb.schemas._enums import SizeType
from themoviedb.schemas._partial import PartialTV, PartialSeason, PartialEpisode
from themoviedb.schemas._result import ResultWithID, ResultWithPage
from themoviedb.schemas.countries import Country
from themoviedb.schemas.genres import Genre
from themoviedb.schemas.languages import Language
from themoviedb.schemas.networks import Network


@dataclass
class CreatedBy:
    id: Optional[int] = None
    credit_id: Optional[str] = None
    name: Optional[str] = None
    gender: Optional[int] = None
    profile_path: Optional[str] = None

    def __str__(self) -> str:
        return self.name

    def profile_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.profile_path}" if self.profile_path else None


@dataclass
class TV(PartialTV):
    created_by: Optional[List[CreatedBy]] = None
    episode_run_time: Optional[List[int]] = None
    genres: Optional[List[Genre]] = None
    homepage: Optional[str] = None
    in_production: Optional[bool] = None
    languages: Optional[List[str]] = None
    last_air_date: Optional[date] = None
    last_episode_to_air: Optional[PartialEpisode] = None
    next_episode_to_air: Optional[None] = None
    networks: Optional[List[Network]] = None
    number_of_episodes: Optional[int] = None
    number_of_seasons: Optional[int] = None
    production_companies: Optional[List[Network]] = None
    production_countries: Optional[List[Country]] = None
    seasons: Optional[List[PartialSeason]] = None
    spoken_languages: Optional[List[Language]] = None
    status: Optional[str] = None
    tagline: Optional[str] = None
    type: Optional[str] = None


@dataclass
class TVs(ResultWithPage):
    results: Optional[List[PartialTV]] = None


@dataclass
class Episodes(ResultWithID):
    results: Optional[List[PartialEpisode]] = None
