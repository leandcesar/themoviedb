# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import List, Optional

from themoviedb.schemas._result import ResultWithID


@dataclass
class ContentRating:
    iso_3166_1: Optional[str] = None
    rating: Optional[str] = None


@dataclass
class ContentRatings(ResultWithID):
    results: Optional[List[ContentRating]] = None
