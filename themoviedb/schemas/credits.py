# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import date
from typing import List, Optional

from themoviedb.schemas._enums import MediaType, SizeType


@dataclass
class Role:
    credit_id: Optional[str] = None
    character: Optional[str] = None
    episode_count: Optional[int] = None


@dataclass
class Job:
    credit_id: Optional[str] = None
    job: Optional[str] = None
    episode_count: Optional[int] = None


@dataclass
class Cast:
    id: Optional[int] = None
    adult: Optional[bool] = None
    gender: Optional[int] = None
    known_for_department: Optional[str] = None
    name: Optional[str] = None
    original_name: Optional[str] = None
    popularity: Optional[float] = None
    profile_path: Optional[str] = None
    cast_id: Optional[int] = None
    character: Optional[str] = None
    credit_id: Optional[str] = None
    order: Optional[int] = None
    total_episode_count: Optional[int] = None
    roles: Optional[List[Role]] = None

    def __str__(self) -> str:
        return self.name or self.original_name or ""

    def profile_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.profile_path}" if self.profile_path else None


@dataclass
class Crew:
    id: Optional[int] = None
    adult: Optional[bool] = None
    gender: Optional[int] = None
    known_for_department: Optional[str] = None
    name: Optional[str] = None
    original_name: Optional[str] = None
    popularity: Optional[float] = None
    profile_path: Optional[str] = None
    credit_id: Optional[str] = None
    department: Optional[str] = None
    job: Optional[str] = None
    total_episode_count: Optional[int] = None
    jobs: Optional[List[Job]] = None
    order: Optional[int] = None

    def __str__(self) -> str:
        return self.name or self.original_name or ""

    def profile_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.profile_path}" if self.profile_path else None


@dataclass
class GuestStars:
    id: Optional[int] = None
    character_name: Optional[str] = None
    credit_id: Optional[str] = None
    order: Optional[int] = None
    adult: Optional[bool] = None
    gender: Optional[int] = None
    known_for_department: Optional[str] = None
    name: Optional[str] = None
    original_name: Optional[str] = None
    popularity: Optional[float] = None
    profile_path: Optional[str] = None


@dataclass
class Credits:
    id: Optional[int] = None
    cast: Optional[List[Cast]] = None
    crew: Optional[List[Crew]] = None
    guest_stars: Optional[List[GuestStars]] = None


@dataclass
class CastMovie:
    id: Optional[int] = None
    character: Optional[str] = None
    credit_id: Optional[str] = None
    release_date: Optional[date] = None
    vote_count: Optional[int] = None
    video: Optional[bool] = None
    adult: Optional[bool] = None
    vote_average: Optional[float] = None
    title: Optional[str] = None
    genre_ids: Optional[List[int]] = None
    original_language: Optional[str] = None
    original_title: Optional[str] = None
    popularity: Optional[float] = None
    backdrop_path: Optional[str] = None
    overview: Optional[str] = None
    poster_path: Optional[str] = None
    order: Optional[int] = None

    def __str__(self) -> str:
        return self.title or ""

    def backdrop_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.backdrop_path}" if self.backdrop_path else None

    def poster_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.poster_path}" if self.poster_path else None


@dataclass
class CrewMovie:
    id: Optional[int] = None
    department: Optional[str] = None
    original_language: Optional[str] = None
    original_title: Optional[str] = None
    job: Optional[str] = None
    overview: Optional[str] = None
    vote_count: Optional[int] = None
    video: Optional[bool] = None
    poster_path: Optional[str] = None
    backdrop_path: Optional[str] = None
    title: Optional[str] = None
    popularity: Optional[float] = None
    genre_ids: Optional[List[int]] = None
    vote_average: Optional[float] = None
    adult: Optional[bool] = None
    release_date: Optional[date] = None
    credit_id: Optional[str] = None
    order: Optional[int] = None

    def __str__(self) -> str:
        return self.title or ""

    def backdrop_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.backdrop_path}" if self.backdrop_path else None

    def poster_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.poster_path}" if self.poster_path else None


@dataclass
class CreditsMovie:
    id: Optional[int] = None
    cast: Optional[List[CastMovie]] = None
    crew: Optional[List[CrewMovie]] = None


@dataclass
class CastTV:
    id: Optional[int] = None
    credit_id: Optional[str] = None
    original_name: Optional[str] = None
    genre_ids: Optional[List[int]] = None
    character: Optional[str] = None
    name: Optional[str] = None
    poster_path: Optional[str] = None
    vote_count: Optional[int] = None
    vote_average: Optional[float] = None
    popularity: Optional[float] = None
    episode_count: Optional[int] = None
    original_language: Optional[str] = None
    adult: Optional[bool] = None
    first_air_date: Optional[date] = None
    backdrop_path: Optional[str] = None
    overview: Optional[str] = None
    origin_country: Optional[List[str]] = None
    order: Optional[int] = None

    def __str__(self) -> str:
        return self.name or self.original_name or ""

    def backdrop_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.backdrop_path}" if self.backdrop_path else None

    def poster_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.poster_path}" if self.poster_path else None


@dataclass
class CrewTV:
    id: Optional[int] = None
    department: Optional[str] = None
    original_language: Optional[str] = None
    episode_count: Optional[int] = None
    job: Optional[str] = None
    overview: Optional[str] = None
    origin_country: Optional[List[str]] = None
    original_name: Optional[str] = None
    genre_ids: Optional[List[int]] = None
    name: Optional[str] = None
    first_air_date: Optional[date] = None
    backdrop_path: Optional[str] = None
    popularity: Optional[float] = None
    adult: Optional[bool] = None
    vote_count: Optional[int] = None
    vote_average: Optional[float] = None
    poster_path: Optional[str] = None
    credit_id: Optional[str] = None
    order: Optional[int] = None

    def __str__(self) -> str:
        return self.name or self.original_name or ""

    def backdrop_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.backdrop_path}" if self.backdrop_path else None

    def poster_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.poster_path}" if self.poster_path else None


@dataclass
class CreditsTV:
    id: Optional[int] = None
    cast: Optional[List[CastTV]] = None
    crew: Optional[List[CrewTV]] = None


@dataclass
class CastCombined(CastMovie, CastTV):
    media_type: Optional[MediaType] = None


@dataclass
class CrewCombined(CrewMovie, CrewTV):
    media_type: Optional[MediaType] = None


@dataclass
class CreditsCombined:
    id: Optional[int] = None
    cast: Optional[List[CastCombined]] = None
    crew: Optional[List[CrewCombined]] = None
