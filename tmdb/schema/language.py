# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class Language:
    english_name: Optional[str]
    iso_639_1: Optional[str]
    name: Optional[str]

    def __str__(self) -> str:
        return self.name
