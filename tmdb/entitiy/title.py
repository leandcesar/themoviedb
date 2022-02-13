# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class Title:
    iso_3166_1: Optional[str]
    title: Optional[str]
    type: Optional[str]

    def __str__(self) -> str:
        return self.title


@dataclass
class Titles:
    id: Optional[int]
    results: Optional[list[Title]]
    titles: Optional[list[Title]]

    def __bool__(self) -> bool:
        return self.results or self.titles

    def __iter__(self) -> iter:
        return iter(self.results or self.titles)

    def __getitem__(self, index: int) -> Title:
        return (self.results or self.titles)[index]
