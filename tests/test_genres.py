from unittest.mock import patch

import pytest

from themoviedb import routes, schemas


@pytest.mark.asyncio
async def test_genres_movie(get_data, assert_data):
    data = get_data("genres/movie_list")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        genres = await routes.Genres().movie()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/genre/movie/list",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(genres, schemas.Genres)
    assert assert_data(genres, data)


@pytest.mark.asyncio
async def test_genres_tv(get_data, assert_data):
    data = get_data("genres/tv_list")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        genres = await routes.Genres().tv()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/genre/tv/list",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(genres, schemas.Genres)
    assert assert_data(genres, data)
