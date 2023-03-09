from dataclasses import dataclass
from datetime import date
from typing import List, Optional

from themoviedb.schemas._enums import SizeType
from themoviedb.schemas.episodes import Episode


@dataclass
class Season:
    id: Optional[int] = None
    _id: Optional[str] = None
    air_date: Optional[date] = None
    episodes: Optional[List[Episode]] = None
    name: Optional[str] = None
    overview: Optional[str] = None
    season_id: Optional[int] = None
    poster_path: Optional[str] = None
    season_number: Optional[int] = None

    def __str__(self) -> str:
        return self.name

    def poster_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.poster_path}" if self.poster_path else None
