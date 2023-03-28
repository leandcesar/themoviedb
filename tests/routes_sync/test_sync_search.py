from unittest.mock import patch

import pytest

from themoviedb import tmdb, schemas


def test_search_collections(get_data, assert_data):
    data = get_data("search/collection")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        collections = tmdb.TMDb().search().collections("test")
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/search/collection",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
                "query": "test",
            },
        )

    assert isinstance(collections, schemas.Collections)
    assert assert_data(collections, data)


def test_search_companies(get_data, assert_data):
    data = get_data("search/company")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        companies = tmdb.TMDb().search().companies("test")
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/search/company",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
                "query": "test",
            },
        )

    assert isinstance(companies, schemas.Companies)
    assert assert_data(companies, data)


def test_search_keywords(get_data, assert_data):
    data = get_data("search/keyword")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        keywords = tmdb.TMDb().search().keywords("test")
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/search/keyword",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
                "query": "test",
            },
        )

    assert isinstance(keywords, schemas.Keywords)
    assert assert_data(keywords, data)


def test_search_movies(get_data, assert_data):
    data = get_data("search/movie")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        movies = tmdb.TMDb().search().movies("test")
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/search/movie",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
                "query": "test",
                "include_adult": False,
            },
        )

    assert isinstance(movies, schemas.Movies)
    assert assert_data(movies, data)


def test_search_multi(get_data, assert_data):
    data = get_data("search/multi")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        multis = tmdb.TMDb().search().multi("test")
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/search/multi",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
                "query": "test",
                "include_adult": False,
            },
        )

    assert isinstance(multis, schemas.Multis)
    assert assert_data(multis, data)


def test_search_people(get_data, assert_data):
    data = get_data("search/person")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        people = tmdb.TMDb().search().people("test")
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/search/person",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
                "query": "test",
                "include_adult": False,
            },
        )

    assert isinstance(people, schemas.People)
    assert assert_data(people, data)


def test_search_tv(get_data, assert_data):
    data = get_data("search/tv")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        tvs = tmdb.TMDb().search().tv("test")
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/search/tv",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
                "query": "test",
                "include_adult": False,
            },
        )

    assert isinstance(tvs, schemas.TVs)
    assert assert_data(tvs, data)
