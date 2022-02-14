# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import date
from typing import Optional

from .company import Company
from .country import Country
from .credit import Credits
from .external_id import ExternalIDs
from .genre import Genre
from .image import Images
from .keyword import Keywords
from .language import Language
from .media import Media
from .provider import Providers
from .title import Titles
from .video import Videos


@dataclass
class Creator:
    id: Optional[int]
    credit_id: Optional[str]
    name: Optional[str]
    gender: Optional[int]
    profile_path: Optional[str]

    def __str__(self) -> str:
        return self.name

    @property
    def profile(self) -> Optional[str]:
        if self.profile_path:
            return f"https://image.tmdb.org/t/p/w1280{self.profile_path}"


@dataclass
class Shows:
    page: Optional[int]
    results: Optional[list[Media]]
    total_pages: Optional[int]
    total_results: Optional[int]

    def __bool__(self) -> bool:
        return self.total_results > 0

    def __iter__(self) -> iter:
        return iter(self.results)

    def __getitem__(self, index: int) -> Media:
        return self.results[index]


@dataclass
class Show:
    id: Optional[int]
    adult: Optional[bool]
    backdrop_path: Optional[str]
    created_by: Optional[list[Creator]]
    episode_run_time: Optional[list[int]]
    first_air_date: Optional[date]
    genres: Optional[list[Genre]]
    homepage: Optional[str]
    in_production: Optional[bool]
    languages: Optional[list[str]]
    last_air_date: Optional[date]
    last_episode_to_air: Optional[Media]
    name: Optional[str]
    networks: Optional[list[Company]]
    next_episode_to_air: Optional[Media]
    number_of_episodes: Optional[int]
    number_of_seasons: Optional[int]
    origin_country: Optional[list[str]]
    original_language: Optional[str]
    original_name: Optional[str]
    overview: Optional[str]
    popularity: Optional[float]
    poster_path: Optional[str]
    production_companies: Optional[list[Company]]
    production_countries: Optional[list[Country]]
    seasons: Optional[list[Media]]
    spoken_languages: Optional[list[Language]]
    status: Optional[str]
    tagline: Optional[str]
    type: Optional[str]
    vote_average: Optional[float]
    vote_count: Optional[int]
    alternative_titles: Optional[Titles]
    credits: Optional[Credits]
    external_ids: Optional[ExternalIDs]
    images: Optional[Images]
    keywords: Optional[Keywords]
    recommendations: Optional[Shows]
    similar: Optional[Shows]
    videos: Optional[Videos]
    watch_providers: Optional[Providers]

    def __post_init__(self) -> None:
        self.name = self.name or self.original_name

    def __str__(self) -> str:
        if self.year:
            return f"{self.name} ({self.year})"
        return self.name

    @property
    def description(self) -> Optional[str]:
        return self.overview

    @property
    def date(self) -> Optional[date]:
        return self.first_air_date

    @property
    def year(self) -> Optional[str]:
        if self.date:
            return str(self.date.year)

    @property
    def rating(self) -> Optional[str]:
        if self.vote_average and self.vote_count:
            return f"{self.vote_average} ({self.vote_count})"
        if self.vote_average:
            return str(self.vote_average)

    @property
    def backdrop(self) -> Optional[str]:
        if self.backdrop_path:
            return f"https://image.tmdb.org/t/p/w1280{self.backdrop_path}"

    @property
    def poster(self) -> Optional[str]:
        if self.poster_path:
            return f"https://image.tmdb.org/t/p/w1280{self.poster_path}"

    @property
    def runtime(self) -> Optional[int]:
        if self.episode_run_time:
            return int(sum(self.episode_run_time) / len(self.episode_run_time))

    @property
    def duration(self) -> Optional[str]:
        if self.runtime:
            hours, minutes = divmod(self.runtime, 60)
            if hours != 0 and minutes != 0:
                return f"{hours}h {minutes}min"
            if hours != 0:
                return f"{hours}h"
            return f"{minutes}min"

    @property
    def duration_total(self) -> Optional[str]:
        if self.runtime and self.number_of_episodes:
            hours, minutes = divmod(self.runtime * self.number_of_episodes, 60)
            if hours != 0 and minutes != 0:
                return f"{hours}h {minutes}min"
            if hours != 0:
                return f"{hours}h"
            return f"{minutes}min"

    @property
    def trailer(self) -> Optional[str]:
        if self.videos and self.videos.results[0].url:
            return self.videos.results[0].url

    @property
    def imdb(self) -> Optional[str]:
        if self.external_ids:
            return self.external_ids.imdb("tv")

    @property
    def directors(self) -> Optional[list[str]]:
        if self.credits:
            return self.credits.directors
