# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional

from .image import Images
from .alternative_name import AlternativeNames


@dataclass
class Company:
    id: Optional[int]
    alternative_names: Optional[AlternativeNames]
    description: Optional[str]
    headquarters: Optional[str]
    homepage: Optional[str]
    images: Optional[Images]
    logo_path: Optional[str]
    name: Optional[str]
    origin_country: Optional[str]
    parent_company: Optional[dict]

    def __str__(self) -> str:
        return self.name

    @property
    def logo(self) -> Optional[str]:
        if self.logo_path:
            return f"https://image.tmdb.org/t/p/w1280{self.logo_path}"


@dataclass
class Companies:
    page: Optional[int]
    results: Optional[list[Company]]
    total_pages: Optional[int]
    total_results: Optional[int]

    def __bool__(self) -> bool:
        return self.total_results > 0

    def __iter__(self) -> iter:
        return iter(self.results)

    def __getitem__(self, index: int) -> Company:
        return self.results[index]
