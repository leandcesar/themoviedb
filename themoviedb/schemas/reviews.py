# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from themoviedb.schemas._enums import MediaType, SizeType
from themoviedb.schemas._result import ResultWithPage


@dataclass
class AuthorDetails:
    name: Optional[str] = None
    username: Optional[str] = None
    avatar_path: Optional[str] = None
    rating: Optional[int] = None

    def __str__(self) -> str:
        return self.name or ""

    def avatar_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.avatar_path}" if self.avatar_path else None


@dataclass
class Review:
    id: Optional[str] = None
    author: Optional[str] = None
    author_details: Optional[AuthorDetails] = None
    content: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    url: Optional[str] = None
    iso_639_1: Optional[str] = None
    media_id: Optional[int] = None
    media_title: Optional[str] = None
    media_type: Optional[MediaType] = None


@dataclass
class Reviews(ResultWithPage):
    results: Optional[List[Review]] = None
