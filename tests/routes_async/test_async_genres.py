from unittest.mock import patch

import pytest

from themoviedb import aiotmdb, schemas


@pytest.mark.asyncio
async def test_genres_movie(get_data, assert_data):
    data = get_data("genres/movie_list")

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        genres = await aiotmdb.aioTMDb().genres().movie()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/genre/movie/list",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(genres, schemas.Genres)
    assert assert_data(genres, data)


@pytest.mark.asyncio
async def test_genres_tv(get_data, assert_data):
    data = get_data("genres/tv_list")

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        genres = await aiotmdb.aioTMDb().genres().tv()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/genre/tv/list",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(genres, schemas.Genres)
    assert assert_data(genres, data)
