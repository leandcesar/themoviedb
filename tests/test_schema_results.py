from types import MappingProxyType
from typing import List

import pytest

from themoviedb import schemas, utils


def test_result_collection_helpers_preserve_list_behavior():
    result = schemas.Result[List[int]](results=[1, 2])

    assert result
    assert list(result) == [1, 2]
    assert result[1] == 2
    assert len(result) == 2


def test_empty_result_collection_helpers_preserve_errors():
    result = schemas.Result[List[int]]()

    assert not result
    assert list(result) == []
    assert len(result) == 0
    with pytest.raises(IndexError, match="Result is empty"):
        result[0]


def test_mapping_result_keeps_region_lookup_and_iteration():
    provider = schemas.WatchProvider(link="https://example.com")
    result = schemas.WatchProviders(results={"BR": provider})

    assert list(result) == ["BR"]
    assert result["BR"] is provider
    assert result.regions == ["BR"]


def test_as_dataclass_accepts_read_only_mappings():
    dates = utils.as_dataclass(
        schemas.Dates,
        MappingProxyType({"minimum": "2024-01-02", "maximum": "2024-01-03"}),
    )

    assert utils.as_dict(dates) == {"maximum": "2024-01-03", "minimum": "2024-01-02"}


def test_movie_duration_formats_more_than_one_hour():
    movie = schemas.Movie(runtime=125)

    assert movie.duration() == "02:05"
    assert movie.duration("%Hh %Mm") == "02h 05m"


def test_tv_duration_formats_total_and_episode_runtime():
    tv = schemas.TV(episode_run_time=[45], number_of_episodes=100)

    assert tv.episode_duration() == "00:45"
    assert tv.duration() == "75:00"
