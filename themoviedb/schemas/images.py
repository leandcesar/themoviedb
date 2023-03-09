from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from themoviedb.schemas._enums import SizeType


@dataclass
class Image:
    id: Optional[str] = None
    aspect_ratio: Optional[float] = None
    file_path: Optional[str] = None
    height: Optional[int] = None
    file_type: Optional[str] = None
    iso_639_1: Optional[str] = None
    vote_average: Optional[float] = None
    vote_count: Optional[int] = None
    width: Optional[int] = None

    def file_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.file_path}" if self.file_path else None


@dataclass
class Images:
    id: Optional[int] = None
    backdrops: Optional[List[Image]] = None
    logos: Optional[List[Image]] = None
    posters: Optional[List[Image]] = None
    profiles: Optional[List[Image]] = None
    stills: Optional[List[Image]] = None
