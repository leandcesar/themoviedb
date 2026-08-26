from unittest.mock import patch

import pytest

from themoviedb import aiotmdb, schemas


@pytest.mark.asyncio
async def test_discover_movie(get_data, assert_data):
    data = get_data("discover/movie")

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        movies = await aiotmdb.aioTMDb().discover().movie()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/discover/movie",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "sort_by": "popularity.desc",
                "page": 1,
            },
        )

    assert isinstance(movies, schemas.Movies)
    assert assert_data(movies, data)


@pytest.mark.asyncio
async def test_discover_tv(get_data, assert_data):
    data = get_data("discover/tv")

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        tvs = await aiotmdb.aioTMDb().discover().tv()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/discover/tv",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "sort_by": "popularity.desc",
                "page": 1,
            },
        )

    assert isinstance(tvs, schemas.TVs)
    assert assert_data(tvs, data)
