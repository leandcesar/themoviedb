from unittest.mock import patch

import pytest

from themoviedb import tmdb, schemas


def test_trending_movie_daily(get_data, assert_data):
    data = get_data("trending/movie")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        movies = tmdb.TMDb().trending().movie_daily()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/trending/movie/day",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
            },
        )

    assert isinstance(movies, schemas.Movies)
    assert assert_data(movies, data)


def test_trending_movie_weekly(get_data, assert_data):
    data = get_data("trending/movie")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        movies = tmdb.TMDb().trending().movie_weekly()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/trending/movie/week",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
            },
        )

    assert isinstance(movies, schemas.Movies)
    assert assert_data(movies, data)


def test_trending_person_daily(get_data, assert_data):
    data = get_data("trending/person")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        people = tmdb.TMDb().trending().person_daily()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/trending/person/day",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
            },
        )

    assert isinstance(people, schemas.People)
    assert assert_data(people, data)


def test_trending_person_weekly(get_data, assert_data):
    data = get_data("trending/person")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        people = tmdb.TMDb().trending().person_weekly()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/trending/person/week",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
            },
        )

    assert isinstance(people, schemas.People)
    assert assert_data(people, data)


def test_trending_tv_daily(get_data, assert_data):
    data = get_data("trending/tv")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        tvs = tmdb.TMDb().trending().tv_daily()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/trending/tv/day",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
            },
        )

    assert isinstance(tvs, schemas.TVs)
    assert assert_data(tvs, data)


def test_trending_tv_weekly(get_data, assert_data):
    data = get_data("trending/tv")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        tvs = tmdb.TMDb().trending().tv_weekly()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/trending/tv/week",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
            },
        )

    assert isinstance(tvs, schemas.TVs)
    assert assert_data(tvs, data)
