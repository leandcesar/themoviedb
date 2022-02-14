# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Video:
    id: Optional[str]
    iso_3166_1: Optional[str]
    iso_639_1: Optional[str]
    key: Optional[str]
    name: Optional[str]
    official: Optional[bool]
    published_at: Optional[date]
    site: Optional[str]
    size: Optional[int]
    type: Optional[str]

    def __str__(self) -> str:
        return self.name

    @property
    def date(self) -> Optional[date]:
        return self.published_at

    @property
    def year(self) -> Optional[str]:
        if self.date:
            return str(self.date.year)

    @property
    def url(self) -> Optional[str]:
        if self.site == "Youtube":
            return f"https://youtube.com/watch?v={self.key}"


@dataclass
class Videos:
    id: Optional[int]
    results: Optional[list[Video]]

    def __bool__(self) -> bool:
        return self.results

    def __iter__(self) -> iter:
        return iter(self.results)

    def __getitem__(self, index: int) -> Video:
        return self.results[index]
