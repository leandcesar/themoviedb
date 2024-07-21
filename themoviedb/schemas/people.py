# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import date
from typing import List, Optional

from themoviedb.schemas._partial import PartialPerson
from themoviedb.schemas._result import ResultWithPage
from themoviedb.schemas.credits import CreditsCombined, CreditsMovie, CreditsTV
from themoviedb.schemas.external_ids import ExternalIDs
from themoviedb.schemas.images import Images, TaggedImages
from themoviedb.schemas.translations import Translations


@dataclass
class Person(PartialPerson):
    birthday: Optional[date] = None
    deathday: Optional[date] = None
    also_known_as: Optional[List[str]] = None
    biography: Optional[str] = None
    place_of_birth: Optional[str] = None
    imdb_id: Optional[str] = None
    homepage: Optional[str] = None
    external_ids: Optional[ExternalIDs] = None
    images: Optional[Images] = None
    combined_credits: Optional[CreditsCombined] = None
    movie_credits: Optional[CreditsMovie] = None
    tv_credits: Optional[CreditsTV] = None
    tagged_images: Optional[TaggedImages] = None
    translations: Optional[Translations] = None

    @property
    def imdb_url(self) -> Optional[str]:
        return f"https://www.imdb.com/name/{self.imdb_id}" if self.imdb_id else None


@dataclass
class People(ResultWithPage):
    results: Optional[List[Person]] = None
