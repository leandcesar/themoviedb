# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional, Union

from themoviedb.schemas._enums import CreditType, MediaType
from themoviedb.schemas._partial import PartialPerson
from themoviedb.schemas.credits import CastMovie, CastTV
from themoviedb.schemas.movies import Movie
from themoviedb.schemas.seasons import Season
from themoviedb.schemas.tv import TV


@dataclass
class FullTV(CastTV, TV, Season):
    ...


@dataclass
class FullMovie(CastMovie, Movie):
    ...


@dataclass
class Credit:
    id: Optional[str] = None
    credit_type: Optional[CreditType] = None
    department: Optional[str] = None
    job: Optional[str] = None
    media: Optional[Union[FullTV, FullMovie]] = None
    media_type: Optional[MediaType] = None
    person: Optional[PartialPerson] = None
