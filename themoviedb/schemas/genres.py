# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import List, Optional

from themoviedb.schemas._result import Result


@dataclass
class Genre:
    id: Optional[int] = None
    name: Optional[str] = None

    def __str__(self) -> str:
        return self.name or ""


@dataclass
class Genres(Result):
    genres: Optional[List[Genre]] = None

    def __post_init__(self) -> None:
        self.results = self.genres
