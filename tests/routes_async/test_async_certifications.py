from unittest.mock import patch

import pytest

from themoviedb import aiotmdb, schemas


@pytest.mark.asyncio
async def test_certifications_movie(get_data, assert_data):
    data = get_data("certifications/movie_list")

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        certifications = await aiotmdb.aioTMDb().certifications().movie()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/certification/movie/list",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            }
        )

    assert isinstance(certifications, schemas.Certifications)
    assert assert_data(certifications, data)


@pytest.mark.asyncio
async def test_certifications_tv(get_data, assert_data):
    data = get_data("certifications/tv_list")

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        certifications = await aiotmdb.aioTMDb().certifications().tv()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/certification/tv/list",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            }
        )
    assert isinstance(certifications, schemas.Certifications)
    assert assert_data(certifications, data)
