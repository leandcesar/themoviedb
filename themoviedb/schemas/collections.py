# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import List, Optional

from themoviedb.schemas._partial import PartialCollection, PartialMovie
from themoviedb.schemas._result import ResultWithPage


@dataclass
class Collection(PartialCollection):
    overview: Optional[str] = None
    parts: Optional[List[PartialMovie]] = None


@dataclass
class Collections(ResultWithPage):
    results: Optional[List[Collection]] = None
