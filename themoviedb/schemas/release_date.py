from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from themoviedb.schemas._result import ResultWithID


@dataclass
class ReleaseDateLocalized:
    certification: Optional[str] = None
    iso_639_1: Optional[str] = None
    release_date: Optional[datetime] = None
    type: Optional[int] = None
    descriptors: Optional[List[str]] = None
    note: Optional[str] = None


@dataclass
class ReleaseDate:
    iso_3166_1: Optional[str] = None
    release_dates: Optional[List[ReleaseDateLocalized]] = None


@dataclass
class ReleaseDates(ResultWithID):
    results: Optional[List[ReleaseDate]] = None
