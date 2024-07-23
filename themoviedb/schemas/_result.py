# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import date
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class Dates:
    maximum: Optional[date] = None
    minimum: Optional[date] = None


@dataclass
class Result(Generic[T]):
    results: Optional[T] = None

    def __bool__(self) -> bool:
        return bool(self.results)

    def __iter__(self):
        if self.results is None:
            return iter([])
        return iter(self.results)

    def __getitem__(self, index):
        if self.results is None:
            raise IndexError("Result is empty")
        return self.results[index]

    def __len__(self) -> int:
        if self.results is None:
            return 0
        return len(self.results)  # type: ignore


@dataclass
class ResultWithID(Result):
    id: Optional[int] = None


@dataclass
class ResultWithPage(ResultWithID):
    page: Optional[int] = None
    dates: Optional[Dates] = None
    total_pages: Optional[int] = None
    total_results: Optional[int] = None
