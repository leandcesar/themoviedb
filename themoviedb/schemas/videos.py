# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from themoviedb.schemas._result import ResultWithID


@dataclass
class Video:
    id: Optional[str] = None
    iso_639_1: Optional[str] = None
    iso_3166_1: Optional[str] = None
    name: Optional[str] = None
    key: Optional[str] = None
    site: Optional[str] = None
    size: Optional[int] = None
    type: Optional[str] = None
    official: Optional[bool] = None
    published_at: Optional[datetime] = None

    def __str__(self) -> str:
        return self.name or ""


@dataclass
class Videos(ResultWithID):
    results: Optional[List[Video]] = None
