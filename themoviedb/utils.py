from dataclasses import asdict
from datetime import date, datetime
from enum import Enum
from typing import Any, Dict, List, Mapping, Tuple, Type, TypeVar

from dacite import Config, from_dict

T = TypeVar("T")
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

config = Config(
    cast=[Enum],
    type_hooks={
        datetime: lambda x: datetime.fromisoformat(x.rstrip("Z")) if x else None,
        date: lambda x: datetime.fromisoformat(x.rstrip("Z")).date() if x else None,
    },
)


def dict_factory(data: List[Tuple[str, Any]]) -> Dict[str, Any]:
    def convert_value(value: Any) -> Any:
        if isinstance(value, Enum):
            return value.value
        if isinstance(value, datetime):
            return f"{value.strftime(DATETIME_FORMAT)[:-3]}Z"
        if isinstance(value, date):
            return value.isoformat()
        return value

    return {k: convert_value(v) for k, v in data}


def as_dataclass(data_class: Type[T], data: Mapping[str, Any]) -> T:
    return from_dict(data_class, data, config=config)


def as_dict(obj: Any) -> Dict[str, Any]:
    return asdict(obj, dict_factory=dict_factory)


def format_duration(minutes: int, fmt: str = "%H:%M") -> str:
    hours, remaining_minutes = divmod(minutes, 60)
    return fmt.replace("%H", "{:02d}".format(hours)).replace("%M", "{:02d}".format(remaining_minutes))
