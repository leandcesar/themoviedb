from dataclasses import dataclass
from typing import Optional, Union

from themoviedb.schemas._enums import CreditType, MediaType
from themoviedb.schemas._partial import PartialPerson
from themoviedb.schemas.credits import CastTV
from themoviedb.schemas.episodes import Episode
from themoviedb.schemas.movies import Movie
from themoviedb.schemas.tv import TV
from themoviedb.schemas.seasons import Season


@dataclass
class CompleteTV(CastTV, TV, Season):
    ...


@dataclass
class Credit:
    id: Optional[str] = None
    credit_type: Optional[CreditType] = None
    department: Optional[str] = None
    job: Optional[str] = None
    media: Optional[Union[CompleteTV, Movie]] = None
    media_type: Optional[MediaType] = None
    person: Optional[PartialPerson] = None
