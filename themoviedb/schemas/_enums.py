from enum import Enum


class CreditType(str, Enum):
    cast = "cast"
    crew = "crew"


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
