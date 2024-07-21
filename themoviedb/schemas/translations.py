# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import List, Optional

from themoviedb.schemas._result import ResultWithID


@dataclass
class Data:
    name: Optional[str] = None
    title: Optional[str] = None
    overview: Optional[str] = None
    homepage: Optional[str] = None
    tagline: Optional[str] = None
    biography: Optional[str] = None


@dataclass
class Translation:
    iso_3166_1: Optional[str] = None
    iso_639_1: Optional[str] = None
    english_name: Optional[str] = None
    name: Optional[str] = None
    data: Optional[Data] = None

    def __str__(self) -> str:
        return self.name or ""


@dataclass
class Translations(ResultWithID):
    translations: Optional[List[Translation]] = None

    def __post_init__(self) -> None:
        self.results = self.translations
