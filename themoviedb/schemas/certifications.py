from dataclasses import dataclass
from typing import Dict, List, Optional

from themoviedb.schemas._result import Result


@dataclass
class Certification:
    certification: Optional[str] = None
    meaning: Optional[str] = None
    order: Optional[int] = None


@dataclass
class Certifications(Result):
    certifications: Optional[Dict[str, List[Certification]]] = None

    def __post_init__(self) -> None:
        self.results = self.certifications

    def __bool__(self) -> bool:
        return bool(self.results)

    def __getitem__(self, region: str) -> List[Certification]:
        return self.results[region]

    @property
    def regions(self) -> List[str]:
        return list(self.results.keys())
