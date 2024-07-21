# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class Change:
    id: Optional[int] = None
    adult: Optional[bool] = None
