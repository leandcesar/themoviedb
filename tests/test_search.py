from unittest.mock import patch

import pytest

from themoviedb import routes, schemas


@pytest.mark.asyncio
async def test_search_collections(get_data, assert_data):
    data = get_data("search/collection")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        collections = await routes.Search().collections("test")
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/search/collection",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
                "query": "test",
            },
        )

    assert isinstance(collections, schemas.Collections)
    assert assert_data(collections, data)


@pytest.mark.asyncio
async def test_search_companies(get_data, assert_data):
    data = get_data("search/company")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        companies = await routes.Search().companies("test")
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/search/company",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
                "query": "test",
            },
        )

    assert isinstance(companies, schemas.Companies)
    assert assert_data(companies, data)


@pytest.mark.asyncio
async def test_search_keywords(get_data, assert_data):
    data = get_data("search/keyword")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        keywords = await routes.Search().keywords("test")
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/search/keyword",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
                "query": "test",
            },
        )

    assert isinstance(keywords, schemas.Keywords)
    assert assert_data(keywords, data)


@pytest.mark.asyncio
async def test_search_movies(get_data, assert_data):
    data = get_data("search/movie")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        movies = await routes.Search().movies("test")
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/search/movie",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
                "query": "test",
                "include_adult": "false",
            },
        )

    assert isinstance(movies, schemas.Movies)
    assert assert_data(movies, data)


@pytest.mark.asyncio
async def test_search_multi(get_data, assert_data):
    data = get_data("search/multi")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        multis = await routes.Search().multi("test")
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/search/multi",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
                "query": "test",
                "include_adult": "false",
            },
        )

    assert isinstance(multis, schemas.Multis)
    assert assert_data(multis, data)


@pytest.mark.asyncio
async def test_search_people(get_data, assert_data):
    data = get_data("search/person")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        people = await routes.Search().people("test")
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/search/person",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
                "query": "test",
                "include_adult": "false",
            },
        )

    assert isinstance(people, schemas.People)
    assert assert_data(people, data)


@pytest.mark.asyncio
async def test_search_tv(get_data, assert_data):
    data = get_data("search/tv")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        tvs = await routes.Search().tv("test")
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/search/tv",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
                "query": "test",
                "include_adult": "false",
            },
        )

    assert isinstance(tvs, schemas.TVs)
    assert assert_data(tvs, data)
