from dataclasses import dataclass
from typing import List, Optional

from themoviedb.schemas._enums import EpisodeGroupType
from themoviedb.schemas._partial import PartialNetwork
from themoviedb.schemas._result import ResultWithID


@dataclass
class EpisodeGroup:
    id: Optional[str] = None
    description: Optional[str] = None
    episode_count: Optional[int] = None
    group_count: Optional[int] = None
    name: Optional[str] = None
    network: Optional[PartialNetwork] = None
    type: Optional[EpisodeGroupType] = None


@dataclass
class EpisodeGroups(ResultWithID):
    results: Optional[List[EpisodeGroup]] = None
