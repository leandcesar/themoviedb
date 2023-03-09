from dataclasses import asdict
from datetime import datetime, date
from enum import Enum
from typing import Type, TypeVar

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

dict_factory = lambda data: dict(
    (
        k,
        v.value
        if isinstance(v, Enum)
        else f"{v.strftime(DATETIME_FORMAT)[:-3]}Z"
        if isinstance(v, datetime)
        else v.isoformat()
        if isinstance(v, date)
        else v,
    )
    for k, v in data
)


def as_dataclass(data_class: Type[T], data: dict) -> T:
    return from_dict(data_class, data, config=config)


def as_dict(obj):
    return asdict(obj, dict_factory=dict_factory)
