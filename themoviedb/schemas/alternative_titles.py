# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import List, Optional

from themoviedb.schemas._result import ResultWithID


@dataclass
class AlternativeTitle:
    iso_3166_1: Optional[str] = None
    title: Optional[str] = None
    type: Optional[str] = None

    def __str__(self) -> str:
        return self.title or ""


@dataclass
class AlternativeTitles(ResultWithID):
    results: Optional[List[AlternativeTitle]] = None
    titles: Optional[List[AlternativeTitle]] = None

    def __post_init__(self) -> None:
        if not self.results and self.titles:
            self.results = self.titles
