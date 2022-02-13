# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class TranslationData:
    homepage: Optional[str]
    overview: Optional[str]
    title: Optional[str]

    def __str__(self) -> str:
        return self.title


@dataclass
class Translation:
    data: Optional[TranslationData]
    english_name: Optional[str]
    iso_3166_1: Optional[str]
    iso_639_1: Optional[str]
    name: Optional[str]

    def __str__(self) -> str:
        return self.name
