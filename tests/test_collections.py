from unittest.mock import patch

import pytest

from themoviedb import tmdb, schemas


@pytest.mark.asyncio
async def test_collection_details(get_data, assert_data):
    data = get_data("collections/details")
    collection_id = 123

    with patch("themoviedb.routes._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        collection = await tmdb.TMDb().collection(collection_id).details()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/collection/{collection_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(collection, schemas.Collection)
    assert assert_data(collection, data)


@pytest.mark.asyncio
async def test_collection_images(get_data, assert_data):
    data = get_data("collections/images")
    collection_id = 123

    with patch("themoviedb.routes._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        images = await tmdb.TMDb().collection(collection_id).images()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/collection/{collection_id}/images",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(images, schemas.Images)
    assert assert_data(images, data)


@pytest.mark.asyncio
async def test_collection_translations(get_data, assert_data):
    data = get_data("collections/translations")
    collection_id = 123

    with patch("themoviedb.routes._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        translations = await tmdb.TMDb().collection(collection_id).translations()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/collection/{collection_id}/translations",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(translations, schemas.Translations)
    assert assert_data(translations, data)
