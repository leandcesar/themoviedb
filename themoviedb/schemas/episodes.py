from dataclasses import dataclass
from datetime import date
from typing import List, Optional

from themoviedb.schemas._enums import SizeType
from themoviedb.schemas.credits import Cast, Crew


@dataclass
class Episode:
    id: Optional[int] = None
    air_date: Optional[date] = None
    episode_number: Optional[int] = None
    crew: Optional[List[Crew]] = None
    guest_stars: Optional[List[Cast]] = None
    name: Optional[str] = None
    overview: Optional[str] = None
    production_code: Optional[str] = None
    season_number: Optional[int] = None
    still_path: Optional[str] = None
    vote_average: Optional[float] = None
    vote_count: Optional[int] = None

    def __str__(self) -> str:
        return self.name

    def still_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.still_path}" if self.still_path else None
