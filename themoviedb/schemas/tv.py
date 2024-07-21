# -*- coding: utf-8 -*-
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, time
from typing import List, Optional

from themoviedb.schemas._enums import SizeType
from themoviedb.schemas._partial import PartialEpisode, PartialSeason, PartialTV
from themoviedb.schemas._result import ResultWithID, ResultWithPage
from themoviedb.schemas.alternative_titles import AlternativeTitles
from themoviedb.schemas.content_ratings import ContentRatings
from themoviedb.schemas.countries import Country
from themoviedb.schemas.credits import Credits
from themoviedb.schemas.episode_groups import EpisodeGroups
from themoviedb.schemas.external_ids import ExternalIDs
from themoviedb.schemas.genres import Genre
from themoviedb.schemas.images import Images
from themoviedb.schemas.keywords import Keywords
from themoviedb.schemas.languages import Language
from themoviedb.schemas.networks import Network
from themoviedb.schemas.reviews import Reviews
from themoviedb.schemas.translations import Translations
from themoviedb.schemas.videos import Videos
from themoviedb.schemas.watch_providers import WatchProviders


@dataclass
class CreatedBy:
    id: Optional[int] = None
    credit_id: Optional[str] = None
    name: Optional[str] = None
    gender: Optional[int] = None
    profile_path: Optional[str] = None

    def __str__(self) -> str:
        return self.name or ""

    def profile_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.profile_path}" if self.profile_path else None


@dataclass
class TVs(ResultWithPage):
    results: Optional[List[PartialTV]] = None


@dataclass
class Episodes(ResultWithID):
    results: Optional[List[PartialEpisode]] = None


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
    next_episode_to_air: Optional[PartialEpisode] = None
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
    aggregate_credits: Optional[Credits] = None
    alternative_titles: Optional[AlternativeTitles] = None
    # changes: Optional[] = None  # TODO
    content_ratings: Optional[ContentRatings] = None
    credits: Optional[Credits] = None
    external_ids: Optional[ExternalIDs] = None
    episode_groups: Optional[EpisodeGroups] = None
    images: Optional[Images] = None
    keywords: Optional[Keywords] = None
    recommendations: Optional[TVs] = None
    reviews: Optional[Reviews] = None
    screened_theatrically: Optional[Episodes] = None
    similar: Optional[TVs] = None
    translations: Optional[Translations] = None
    videos: Optional[Videos] = None
    watch_providers: Optional[WatchProviders] = None

    @property
    def run_time(self) -> Optional[int]:
        if self.episode_run_time and self.number_of_episodes:
            run_time = self.episode_run_time[0] * self.number_of_episodes
            return run_time
        return None

    def episode_duration(self, fmt: str = "%H:%M") -> Optional[str]:
        if self.run_time and self.number_of_episodes:
            run_time_average = self.run_time // self.number_of_episodes
            return time(minute=run_time_average).strftime(fmt)
        return None

    def duration(self, fmt: str = "%H:%M") -> Optional[str]:
        if self.run_time:
            return time(minute=self.run_time).strftime(fmt)
        return None
