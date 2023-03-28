from unittest.mock import patch

import pytest

from themoviedb import tmdb, schemas


def test_watch_providers_movie(get_data, assert_data):
    data = get_data("watch_providers/movie")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        watch_providers = tmdb.TMDb().watch_providers().movie()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/watch/providers/movie",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            }
        )

    assert isinstance(watch_providers, schemas.WatchProvidersData)
    assert assert_data(watch_providers, data)


def test_watch_providers_regions(get_data, assert_data):
    data = get_data("watch_providers/regions")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        regions = tmdb.TMDb().watch_providers().regions()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/watch/providers/regions",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            }
        )

    assert isinstance(regions, schemas.Regions)
    assert assert_data(regions, data)


def test_watch_providers_tv(get_data, assert_data):
    data = get_data("watch_providers/tv")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        watch_providers = tmdb.TMDb().watch_providers().tv()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/watch/providers/tv",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            }
        )
    assert isinstance(watch_providers, schemas.WatchProvidersData)
    assert assert_data(watch_providers, data)
