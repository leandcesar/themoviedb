# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional

from .image import Images
from .media import Media
from .translaction import Translation


@dataclass
class Collection:
    id: Optional[int]
    adult: Optional[bool]
    backdrop_path: Optional[str]
    images: Optional[Images]
    name: Optional[str]
    original_language: Optional[str]
    original_name: Optional[str]
    overview: Optional[str]
    parts: Optional[list[Media]]
    poster_path: Optional[str]
    translations: Optional[list[Translation]]

    def __post_init__(self) -> None:
        self.name = self.name or self.original_name

    def __str__(self) -> str:
        return self.name

    @property
    def backdrop(self) -> Optional[str]:
        if self.backdrop_path:
            return f"https://image.tmdb.org/t/p/w1280{self.backdrop_path}"

    @property
    def poster(self) -> Optional[str]:
        if self.poster_path:
            return f"https://image.tmdb.org/t/p/w1280{self.poster_path}"


@dataclass
class Collections:
    page: Optional[int]
    results: Optional[list[Collection]]
    total_pages: Optional[int]
    total_results: Optional[int]

    def __bool__(self) -> bool:
        return self.total_results > 0

    def __iter__(self) -> iter:
        return iter(self.results)

    def __getitem__(self, index: int) -> Collection:
        return self.results[index]
