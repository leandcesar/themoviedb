from enum import Enum


class CreditType(str, Enum):
    cast = "cast"
    crew = "crew"


class EpisodeGroupType(Enum):
    original_air_date = 1
    absolute = 2
    dvd = 3
    digital = 4
    story_arc = 5
    production = 6
    tv = 7

    __str_map__ = {
        1: "Original air date",
        2: "Absolute",
        3: "DVD",
        4: "Digital",
        5: "Story arc",
        6: "Production",
        7: "TV",
    }

    def __str__(self) -> str:
        return self.__str_map__[self.value]


class ImageType(str, Enum):
    backdrop = "backdrop"
    logo = "logo"
    poster = "poster"
    profile = "profile"
    still = "still"


class MediaType(str, Enum):
    movie = "movie"
    person = "person"
    tv = "tv"


class SizeType(str, Enum):
    w45 = "w45"
    w92 = "w92"
    w154 = "w154"
    w185 = "w185"
    w300 = "w300"
    w342 = "w342"
    w500 = "w500"
    h632 = "h632"
    w780 = "w780"
    w1280 = "w1280"
    original = "original"
