# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import date
from typing import Optional

from .external_id import ExternalIDs
from .image import Images
from .media import Media


# @dataclass
# class Person:
#     id: Optional[int]
#     gender: Optional[int]
#     name: Optional[str]
#     known_for_department: Optional[str]
#     profile_path: Optional[str]
#     known_for: Optional[list[Media]]
#     adult: Optional[bool]
#     popularity: Optional[float]

#     @property
#     def profile(self) -> Optional[str]:
#         if self.profile_path:
#             return f"https://image.tmdb.org/t/p/w1280{self.profile_path}"


# @dataclass
# class Job:
#     id: Optional[str]
#     credit_type: Optional[str]
#     department: Optional[str]
#     job: Optional[str]
#     media: Optional[Media]
#     media_type: Optional[str]
#     person: Optional[Person]


@dataclass
class PersonPartial:
    id: Optional[int]
    adult: Optional[bool]
    gender: Optional[int]
    known_for: Optional[list[Media]]
    known_for_department: Optional[str]
    name: Optional[str]
    popularity: Optional[float]
    profile_path: Optional[str]

    def __str__(self) -> str:
        return self.name

    @property
    def profile(self) -> Optional[str]:
        if self.profile_path:
            return f"https://image.tmdb.org/t/p/w1280{self.profile_path}"


@dataclass
class Job:
    id: Optional[int]
    adult: Optional[bool]
    backdrop_path: Optional[str]
    character: Optional[str]
    credit_id: Optional[str]
    department: Optional[str]
    episode_count: Optional[int]
    first_air_date: Optional[date]
    genre_ids: Optional[list[int]]
    job: Optional[str]
    media_type: Optional[str]
    name: Optional[str]
    order: Optional[int]
    origin_country: Optional[list[str]]
    original_language: Optional[str]
    original_name: Optional[str]
    original_title: Optional[str]
    overview: Optional[str]
    popularity: Optional[float]
    poster_path: Optional[str]
    release_date: Optional[date]
    title: Optional[str]
    video: Optional[bool]
    vote_average: Optional[float]
    vote_count: Optional[int]

    def __post_init__(self) -> None:
        self.name = self.title or self.name or self.original_title or self.original_name

    def __str__(self) -> str:
        if self.year:
            return f"{self.name} ({self.year})"
        return self.name

    @property
    def description(self) -> Optional[str]:
        return self.overview

    @property
    def date(self) -> Optional[date]:
        return self.release_date or self.first_air_date

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


@dataclass
class Jobs:
    id: Optional[int]
    cast: Optional[list[Job]]
    crew: Optional[list[Job]]

    def __bool__(self) -> bool:
        return self.cast or self.crew


@dataclass
class People:
    page: Optional[int]
    results: Optional[list[PersonPartial]]
    total_pages: Optional[int]
    total_results: Optional[int]

    def __bool__(self) -> bool:
        return self.total_results > 0

    def __iter__(self) -> iter:
        return iter(self.results)

    def __getitem__(self, index: int) -> PersonPartial:
        return self.results[index]


@dataclass
class Person:
    id: Optional[int]
    adult: Optional[bool]
    also_known_as: Optional[list[str]]
    biography: Optional[str]
    birthday: Optional[date]
    deathday: Optional[date]
    gender: Optional[int]
    homepage: Optional[str]
    imdb_id: Optional[str]
    known_for_department: Optional[str]
    name: Optional[str]
    place_of_birth: Optional[str]
    popularity: Optional[float]
    profile_path: Optional[str]
    combined_credits: Optional[Jobs]
    external_ids: Optional[ExternalIDs]
    images: Optional[Images]
    movie_credits: Optional[Jobs]
    tv_credits: Optional[Jobs]

    def __str__(self) -> str:
        return self.name

    @property
    def description(self) -> Optional[str]:
        return self.biography

    @property
    def date(self) -> Optional[date]:
        return self.birthday

    @property
    def year(self) -> Optional[str]:
        if self.date:
            return str(self.date.year)

    @property
    def age(self) -> Optional[str]:
        age = date.today() - self.birthday
        return age.year

    @property
    def known_for(self) -> Optional[list[Job]]:
        if self.known_for_department == "Acting":
            return self.combined_credits.cast
        return self.combined_credits.crew

    @property
    def profile(self) -> Optional[str]:
        if self.backdrop_path:
            return f"https://image.tmdb.org/t/p/w1280{self.profile_path}"

    @property
    def imdb(self) -> Optional[str]:
        if self.external_ids:
            return self.external_ids.imdb("person")
