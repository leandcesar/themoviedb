# -*- coding: utf-8 -*-
from unittest.mock import patch

import pytest

from themoviedb import aiotmdb, schemas


@pytest.mark.asyncio
async def test_network_details(get_data, assert_data):
    data = get_data("networks/details")
    network_id = 123

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        network = await aiotmdb.aioTMDb().network(network_id).details()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/network/{network_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(network, schemas.Network)
    assert assert_data(network, data)


@pytest.mark.asyncio
async def test_network_alternative_names(get_data, assert_data):
    data = get_data("networks/alternative_names")
    network_id = 123

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        alternative_names = await aiotmdb.aioTMDb().network(network_id).alternative_names()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/network/{network_id}/alternative_names",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(alternative_names, schemas.AlternativeNames)
    assert assert_data(alternative_names, data)


@pytest.mark.asyncio
async def test_network_images(get_data, assert_data):
    data = get_data("networks/images")
    network_id = 123

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        images = await aiotmdb.aioTMDb().network(network_id).images()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/network/{network_id}/images",
            params={
                "api_key": "TEST_TMDB_KEY",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(images, schemas.Images)
    assert assert_data(images, data)
