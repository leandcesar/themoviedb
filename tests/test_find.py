from unittest.mock import patch

import pytest

from themoviedb import routes, schemas


@pytest.mark.asyncio
async def test_find_by_facebook(get_data, assert_data):
    data = get_data("find/find")
    facebook_id = "test"

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        results = await routes.Find().by_facebook(facebook_id)
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/find/{facebook_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "external_source": "facebook_id",
            },
        )

    assert isinstance(results, schemas.MultiResults)
    assert assert_data(results, data)


@pytest.mark.asyncio
async def test_find_by_imdb(get_data, assert_data):
    data = get_data("find/find")
    imdb_id = "test"

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        results = await routes.Find().by_imdb(imdb_id)
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/find/{imdb_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "external_source": "imdb_id",
            },
        )

    assert isinstance(results, schemas.MultiResults)
    assert assert_data(results, data)
