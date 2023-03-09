from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from themoviedb.schemas._partial import PartialMovie
from themoviedb.schemas._result import ResultWithPage
from themoviedb.schemas.alternative_titles import AlternativeTitles
from themoviedb.schemas.collections import Collection
from themoviedb.schemas.companies import Company
from themoviedb.schemas.countries import Country
from themoviedb.schemas.credits import Credits
from themoviedb.schemas.external_ids import ExternalIDs
from themoviedb.schemas.genres import Genre
from themoviedb.schemas.images import Images
from themoviedb.schemas.keywords import Keywords
from themoviedb.schemas.languages import Language
from themoviedb.schemas.videos import Videos
from themoviedb.schemas.watch_providers import WatchProviders


@dataclass
class Movie(PartialMovie):
    belongs_to_collection: Optional[Collection] = None
    budget: Optional[int] = None
    genres: Optional[List[Genre]] = None
    homepage: Optional[str] = None
    imdb_id: Optional[str] = None
    production_companies: Optional[List[Company]] = None
    production_countries: Optional[List[Country]] = None
    revenue: Optional[int] = None
    runtime: Optional[int] = None
    spoken_languages: Optional[List[Language]] = None
    status: Optional[str] = None
    tagline: Optional[str] = None
    alternative_titles: Optional[AlternativeTitles] = None
    # changes = Optional[] = None  # TODO
    credits: Optional[Credits] = None
    external_ids: Optional[ExternalIDs] = None
    images: Optional[Images] = None
    keywords: Optional[Keywords] = None
    # lists = Optional[] = None  # TODO
    recommendations: Optional[Movies] = None
    # release_dates = Optional[] = None  # TODO
    # reviews = Optional[] = None  # TODO
    similar: Optional[Movies] = None
    # translations = Optional[] = None  # TODO
    videos: Optional[Videos] = None
    watch_providers: Optional[WatchProviders] = None

    @property
    def imdb(self) -> Optional[str]:
        return f"https://www.imdb.com/title/{self.imdb_id}" if self.imdb_id else None


@dataclass
class Movies(ResultWithPage):
    results: Optional[List[PartialMovie]] = None
