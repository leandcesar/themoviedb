from dataclasses import dataclass
from typing import Optional

from themoviedb.schemas._enums import SizeType


@dataclass
class Network:
    id: int
    headquarters: Optional[str] = None
    homepage: Optional[str] = None
    logo_path: Optional[str] = None
    name: Optional[str] = None
    origin_country: Optional[str] = None

    def __str__(self) -> str:
        return self.name

    def logo_url(self, size: Optional[SizeType] = SizeType.original) -> Optional[str]:
        return f"https://image.tmdb.org/t/p/{size}{self.logo_path}" if self.logo_path else None
