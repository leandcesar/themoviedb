from dataclasses import dataclass
from typing import Optional

from themoviedb.schemas._partial import PartialNetwork


@dataclass
class Network(PartialNetwork):
    headquarters: Optional[str] = None
    homepage: Optional[str] = None
