from dataclasses import dataclass
from typing import Optional


@dataclass
class Change:
    id: int
    adult: Optional[bool] = None
