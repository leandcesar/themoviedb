# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import List, Optional

from themoviedb.schemas._enums import EpisodeGroupType
from themoviedb.schemas._partial import PartialEpisode, PartialNetwork
from themoviedb.schemas._result import ResultWithID


@dataclass
class Group:
    id: Optional[str] = None
    name: Optional[str] = None
    order: Optional[int] = None
    episodes: Optional[List[PartialEpisode]] = None
    locked: Optional[bool] = None


@dataclass
class EpisodeGroup:
    id: Optional[str] = None
    description: Optional[str] = None
    episode_count: Optional[int] = None
    group_count: Optional[int] = None
    groups: Optional[List[Group]] = None
    name: Optional[str] = None
    network: Optional[PartialNetwork] = None
    type: Optional[EpisodeGroupType] = None


@dataclass
class EpisodeGroups(ResultWithID):
    results: Optional[List[EpisodeGroup]] = None
