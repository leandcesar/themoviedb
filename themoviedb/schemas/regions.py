from dataclasses import dataclass
from typing import List, Optional

from themoviedb.schemas._result import Result


@dataclass
class Region:
    iso_3166_1: Optional[str] = None
    english_name: Optional[str] = None
    native_name: Optional[str] = None

    def __str__(self) -> str:
        return self.native_name


@dataclass
class Regions(Result):
    results: Optional[List[Region]] = None
