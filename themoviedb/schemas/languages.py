# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class Language:
    english_name: Optional[str] = None
    iso_639_1: Optional[str] = None
    name: Optional[str] = None

    def __str__(self) -> str:
        return self.name or ""
