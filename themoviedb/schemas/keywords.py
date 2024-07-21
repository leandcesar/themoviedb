# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import List, Optional

from themoviedb.schemas._partial import PartialKeyword
from themoviedb.schemas._result import ResultWithPage


@dataclass
class Keyword(PartialKeyword):
    ...


@dataclass
class Keywords(ResultWithPage):
    keywords: Optional[List[Keyword]] = None
    results: Optional[List[Keyword]] = None

    def __post_init__(self) -> None:
        self.results = self.keywords or self.results
