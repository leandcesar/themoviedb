# -*- coding: utf-8 -*-
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from themoviedb.schemas._partial import PartialCompany
from themoviedb.schemas._result import ResultWithPage


@dataclass
class Company(PartialCompany):
    description: Optional[str] = None
    headquarters: Optional[str] = None
    homepage: Optional[str] = None
    origin_country: Optional[str] = None
    parent_company: Optional[Company] = None


@dataclass
class Companies(ResultWithPage):
    results: Optional[List[Company]] = None
