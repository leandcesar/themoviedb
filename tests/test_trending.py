from unittest.mock import patch

import pytest

from themoviedb import routes, schemas


@pytest.mark.asyncio
async def test_trending_movie_daily(get_data, assert_data):
    data = get_data("trending/movie")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        movies = await routes.Trending().movie_daily()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/trending/movie/day",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
            },
        )

    assert isinstance(movies, schemas.Movies)
    assert assert_data(movies, data)


@pytest.mark.asyncio
async def test_trending_movie_weekly(get_data, assert_data):
    data = get_data("trending/movie")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        movies = await routes.Trending().movie_weekly()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/trending/movie/week",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
            },
        )

    assert isinstance(movies, schemas.Movies)
    assert assert_data(movies, data)


@pytest.mark.asyncio
async def test_trending_person_daily(get_data, assert_data):
    data = get_data("trending/person")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        people = await routes.Trending().person_daily()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/trending/person/day",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
            },
        )

    assert isinstance(people, schemas.People)
    assert assert_data(people, data)


@pytest.mark.asyncio
async def test_trending_person_weekly(get_data, assert_data):
    data = get_data("trending/person")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        people = await routes.Trending().person_weekly()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/trending/person/week",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
            },
        )

    assert isinstance(people, schemas.People)
    assert assert_data(people, data)


@pytest.mark.asyncio
async def test_trending_tv_daily(get_data, assert_data):
    data = get_data("trending/tv")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        tvs = await routes.Trending().tv_daily()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/trending/tv/day",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
            },
        )

    assert isinstance(tvs, schemas.TVs)
    assert assert_data(tvs, data)


@pytest.mark.asyncio
async def test_trending_tv_weekly(get_data, assert_data):
    data = get_data("trending/tv")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        tvs = await routes.Trending().tv_weekly()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/trending/tv/week",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
            },
        )

    assert isinstance(tvs, schemas.TVs)
    assert assert_data(tvs, data)
