from dataclasses import dataclass
from typing import List, Optional

from themoviedb.schemas._result import ResultWithID


@dataclass
class AlternativeName:
    name: Optional[str] = None
    type: Optional[str] = None

    def __str__(self) -> str:
        return self.name


@dataclass
class AlternativeNames(ResultWithID):
    results: Optional[List[AlternativeName]] = None
