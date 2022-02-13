# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class Country:
    iso_3166_1: Optional[str]
    name: Optional[str]

    def __str__(self) -> str:
        return self.name
