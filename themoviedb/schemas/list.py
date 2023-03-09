from dataclasses import dataclass
from typing import List, Optional

from themoviedb.schemas._enums import SizeType
from themoviedb.schemas._result import ResultWithPage


@dataclass
class ItemList:
    id: int
    description: Optional[str] = None
    favorite_count: Optional[int] = None
    item_count: Optional[int] = None
    iso_639_1: Optional[str] = None
    list_type: Optional[str] = None
    name: Optional[str] = None
    poster_path: Optional[str] = None

    def __str__(self) -> str:
        return self.name

    def poster_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.poster_path}" if self.poster_path else None


@dataclass
class ItemsList(ResultWithPage):
    results: Optional[List[ItemList]] = None
