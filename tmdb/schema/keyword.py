# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class Keyword:
    id: Optional[int]
    name: Optional[str]

    def __str__(self) -> str:
        return self.name


@dataclass
class Keywords:
    id: Optional[int]
    keywords: Optional[list[Keyword]]
    page: Optional[int]
    results: Optional[list[Keyword]]
    total_pages: Optional[int]
    total_results: Optional[int]

    def __bool__(self) -> bool:
        return self.total_results > 0

    def __iter__(self) -> iter:
        return iter(self.results or self.keywords)

    def __getitem__(self, index: int) -> Keyword:
        return (self.keywords or self.results)[index]
