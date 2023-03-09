from dataclasses import dataclass
from typing import Optional


@dataclass
class Country:
    iso_3166_1: Optional[str] = None
    name: Optional[str] = None

    def __str__(self) -> str:
        return self.name
