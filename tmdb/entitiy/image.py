# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class Image:
    aspect_ratio: Optional[float]
    file_path: Optional[str]
    height: Optional[int]
    iso_639_1: Optional[str]
    vote_average: Optional[float]
    vote_count: Optional[int]
    width: Optional[int]

    def __str__(self) -> str:
        return self.file

    @property
    def file(self) -> Optional[str]:
        if self.file_path:
            return f"https://image.tmdb.org/t/p/w1280{self.file_path}"

    @property
    def rating(self) -> Optional[str]:
        if self.vote_average and self.vote_count:
            return f"{self.vote_average} ({self.vote_count})"
        if self.vote_average:
            return str(self.vote_average)


@dataclass
class Images:
    id: Optional[int]
    backdrops: Optional[list[Image]]
    logos: Optional[list[Image]]
    posters: Optional[list[Image]]
    profiles: Optional[list[Image]]

    def __bool__(self) -> bool:
        return (
            self.backdrops
            or self.logos
            or self.posters
            or self.tv_results
            or self.profiles
        )
