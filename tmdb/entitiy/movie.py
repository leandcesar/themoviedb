# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import date
from typing import Optional

from .collection import Collection
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
class Movies:
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
class Movie:
    id: Optional[int]
    adult: Optional[bool]
    backdrop_path: Optional[str]
    belongs_to_collection: Optional[Collection]
    budget: Optional[int]
    genres: Optional[list[Genre]]
    homepage: Optional[str]
    imdb_id: Optional[str]
    original_language: Optional[str]
    original_title: Optional[str]
    overview: Optional[str]
    popularity: Optional[float]
    poster_path: Optional[str]
    production_companies: Optional[list[Company]]
    production_countries: Optional[list[Country]]
    release_date: Optional[date]
    revenue: Optional[int]
    runtime: Optional[int]
    spoken_languages: Optional[list[Language]]
    status: Optional[str]
    tagline: Optional[str]
    title: Optional[str]
    video: Optional[bool]
    vote_average: Optional[float]
    vote_count: Optional[int]
    alternative_titles: Optional[Titles]
    credits: Optional[Credits]
    external_ids: Optional[ExternalIDs]
    images: Optional[Images]
    keywords: Optional[Keywords]
    recommendations: Optional[Movies]
    similar: Optional[Movies]
    videos: Optional[Videos]
    watch_providers: Optional[Providers]

    def __str__(self) -> str:
        if self.year:
            return f"{self.name} ({self.year})"
        return self.name

    @property
    def name(self) -> str:
        return self.title or self.original_title

    @property
    def original_name(self) -> str:
        return self.original_title

    @property
    def description(self) -> Optional[str]:
        return self.overview

    @property
    def date(self) -> Optional[date]:
        return self.release_date

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
    def duration(self) -> Optional[str]:
        if self.runtime:
            hours, minutes = divmod(self.runtime, 60)
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
            return self.external_ids.imdb("movie")

    @property
    def directors(self) -> Optional[list[str]]:
        if self.credits:
            return self.credits.directors
