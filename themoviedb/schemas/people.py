from datetime import date
from dataclasses import dataclass
from typing import List, Optional

from themoviedb.schemas._partial import PartialPerson
from themoviedb.schemas._result import ResultWithPage


@dataclass
class Person(PartialPerson):
    birthday: Optional[date] = None
    deathday: Optional[date] = None
    also_known_as: Optional[List[str]] = None
    biography: Optional[str] = None
    place_of_birth: Optional[str] = None
    imdb_id: Optional[str] = None
    homepage: Optional[str] = None

    @property
    def imdb(self) -> Optional[str]:
        return f"https://www.imdb.com/name/{self.imdb_id}" if self.imdb_id else None


@dataclass
class People(ResultWithPage):
    results: Optional[List[Person]] = None
