# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class Data:
    display_priority: Optional[int]
    logo_path: Optional[str]
    provider_id: Optional[int]
    provider_name: Optional[str]

    def __str__(self) -> str:
        return self.provider_name

    @property
    def logo(self) -> Optional[str]:
        if self.logo_path:
            return f"https://image.tmdb.org/t/p/w1280{self.logo_path}"


@dataclass
class ProviderData:
    buy: Optional[list[Data]]
    flatrate: Optional[list[Data]]
    free: Optional[list[Data]]
    link: Optional[str]

    def __str__(self) -> str:
        return self.link

    def __bool__(self) -> bool:
        return self.buy or self.flatrate or self.free


@dataclass
class Provider:
    BR: Optional[ProviderData]
    US: Optional[ProviderData]


@dataclass
class Providers:
    id: Optional[int]
    results: Optional[Provider]

    def __bool__(self) -> bool:
        return self.results

    def __getitem__(self, region: str) -> ProviderData:
        return self.results[region.upper()]
