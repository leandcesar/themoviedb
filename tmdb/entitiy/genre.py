# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class Genre:
    id: Optional[int]
    name: Optional[str]

    def __str__(self) -> str:
        return self.name
