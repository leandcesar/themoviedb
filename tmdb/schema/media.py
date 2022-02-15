# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import date
from typing import Optional, Union


@dataclass
class Media:
    id: Optional[Union[int, float]]
    adult: Optional[bool]
    air_date: Optional[date]
    backdrop_path: Optional[str]
    character: Optional[str]
    episode_count: Optional[int]
    episode_number: Optional[int]
    first_air_date: Optional[date]
    genre_ids: Optional[list[Union[int, float]]]
    media_type: Optional[str]
    name: Optional[str]
    origin_country: Optional[list[str]]
    original_language: Optional[str]
    original_name: Optional[str]
    original_title: Optional[str]
    overview: Optional[str]
    popularity: Optional[float]
    poster_path: Optional[str]
    production_code: Optional[str]
    release_date: Optional[date]
    season_number: Optional[int]
    still_path: Optional[str]
    title: Optional[str]
    video: Optional[bool]
    vote_average: Optional[float]
    vote_count: Optional[Union[int, float]]

    def __post_init__(self) -> None:
        self.id = int(self.id)
        self.vote_count = int(self.vote_count)
        self.genre_ids = [int(genre_id) for genre_id in self.genre_ids]
        self.name = self.title or self.name or self.original_title or self.original_name
        self.original_name = self.original_title or self.original_name
        self.media_type = "movie" if self.original_title else "tv"

    def __str__(self) -> str:
        if self.year:
            return f"{self.name} ({self.year})"
        return self.name

    @property
    def description(self) -> Optional[str]:
        return self.overview

    @property
    def date(self) -> Optional[date]:
        return self.release_date or self.first_air_date or self.air_date

    @property
    def year(self) -> Optional[str]:
        if self.date:
            return str(self.date.year)

    @property
    def rating(self) -> Optional[str]:
        if self.vote_average and self.vote_count:
            return f"{self.vote_average} ({self.vote_count})"
        if self.vote_average:
            return str(self.vote_average)

    @property
    def backdrop(self) -> Optional[str]:
        if self.backdrop_path:
            return f"https://image.tmdb.org/t/p/w1280{self.backdrop_path}"

    @property
    def poster(self) -> Optional[str]:
        if self.poster_path:
            return f"https://image.tmdb.org/t/p/w1280{self.poster_path}"
