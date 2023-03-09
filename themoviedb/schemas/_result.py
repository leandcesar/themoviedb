from dataclasses import dataclass
from datetime import date
from typing import List, Optional, Type, TypeVar

T = TypeVar("T")


@dataclass
class Dates:
    maximum: Optional[date] = None
    minimum: Optional[date] = None


@dataclass
class Result:
    results: Optional[List[Type[T]]] = None

    def __bool__(self) -> bool:
        return len(self.results) > 0

    def __iter__(self) -> iter:
        return iter(self.results)

    def __getitem__(self, index: int) -> T:
        return self.results[index]

    def __len__(self) -> int:
        return len(self.results)


@dataclass
class ResultWithID(Result):
    id: Optional[int] = None


@dataclass
class ResultWithPage(ResultWithID):
    page: Optional[int] = None
    dates: Optional[Dates] = None
    total_pages: Optional[int] = None
    total_results: Optional[int] = None
