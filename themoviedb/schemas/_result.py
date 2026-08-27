from dataclasses import dataclass
from datetime import date
from typing import Any, Generic, Iterable, Iterator, Optional, Sized, TypeVar, cast

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

    def __iter__(self) -> Iterator[Any]:
        if self.results is None:
            return iter(())
        return iter(cast(Iterable[Any], self.results))

    def __getitem__(self, index: Any) -> Any:
        if self.results is None:
            raise IndexError("Result is empty")
        return cast(Any, self.results)[index]

    def __len__(self) -> int:
        if self.results is None:
            return 0
        return len(cast(Sized, self.results))


@dataclass
class ResultWithID(Result[T], Generic[T]):
    id: Optional[int] = None


@dataclass
class ResultWithPage(ResultWithID[T], Generic[T]):
    page: Optional[int] = None
    dates: Optional[Dates] = None
    total_pages: Optional[int] = None
    total_results: Optional[int] = None
