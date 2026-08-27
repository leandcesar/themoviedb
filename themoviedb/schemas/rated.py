from dataclasses import dataclass
from typing import List, Optional

from themoviedb.schemas._partial import PartialEpisode, PartialMovie, PartialTV
from themoviedb.schemas._result import ResultWithPage


@dataclass
class RatedMovie(PartialMovie):
    rating: Optional[float] = None


@dataclass
class RatedMovies(ResultWithPage[List[RatedMovie]]):
    results: Optional[List[RatedMovie]] = None


@dataclass
class RatedTV(PartialTV):
    rating: Optional[float] = None


@dataclass
class RatedTVs(ResultWithPage[List[RatedTV]]):
    results: Optional[List[RatedTV]] = None


@dataclass
class RatedEpisode(PartialEpisode):
    rating: Optional[float] = None


@dataclass
class RatedEpisodes(ResultWithPage[List[RatedEpisode]]):
    results: Optional[List[RatedEpisode]] = None
