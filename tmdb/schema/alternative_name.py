# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class AlternativeName:
    name: Optional[str]
    type: Optional[str]

    def __str__(self) -> str:
        return self.name


@dataclass
class AlternativeNames:
    id: Optional[int]
    alternative_names: Optional[list[AlternativeName]]
    results: Optional[list[AlternativeName]]

    def __bool__(self) -> bool:
        return self.alternative_names or self.results

    def __iter__(self) -> iter:
        return iter(self.alternative_names or self.results)

    def __getitem__(self, index: int) -> AlternativeName:
        return (self.alternative_names or self.results)[index]
