from unittest.mock import patch

import pytest

from themoviedb import tmdb, schemas


def test_discover_movie(get_data, assert_data):
    data = get_data("discover/movie")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        movies = tmdb.TMDb().discover().movie()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/discover/movie",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "sort_by": "popularity.desc",
                "page": 1,
            },
        )

    assert isinstance(movies, schemas.Movies)
    assert assert_data(movies, data)


def test_discover_tv(get_data, assert_data):
    data = get_data("discover/tv")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        tvs = tmdb.TMDb().discover().tv()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/discover/tv",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "sort_by": "popularity.desc",
                "page": 1,
            },
        )

    assert isinstance(tvs, schemas.TVs)
    assert assert_data(tvs, data)
