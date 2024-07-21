# -*- coding: utf-8 -*-
from unittest.mock import patch

from themoviedb import schemas, tmdb


def test_find_by_imdb(get_data, assert_data):
    data = get_data("find/find")
    imdb_id = "test"

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        results = tmdb.TMDb().find().by_imdb(imdb_id)
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/find/{imdb_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "external_source": "imdb_id",
            },
        )

    assert isinstance(results, schemas.MultiResults)
    assert assert_data(results, data)


def test_find_by_tvdb(get_data, assert_data):
    data = get_data("find/find")
    tvdb_id = "test"

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        results = tmdb.TMDb().find().by_tvdb(tvdb_id)
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/find/{tvdb_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "external_source": "tvdb_id",
            },
        )

    assert isinstance(results, schemas.MultiResults)
    assert assert_data(results, data)


def test_find_by_freebase_mid(get_data, assert_data):
    data = get_data("find/find")
    freebase_mid = "test"

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        results = tmdb.TMDb().find().by_freebase_mid(freebase_mid)
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/find/{freebase_mid}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "external_source": "freebase_mid",
            },
        )

    assert isinstance(results, schemas.MultiResults)
    assert assert_data(results, data)


def test_find_by_freebase(get_data, assert_data):
    data = get_data("find/find")
    freebase_id = "test"

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        results = tmdb.TMDb().find().by_freebase(freebase_id)
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/find/{freebase_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "external_source": "freebase_id",
            },
        )

    assert isinstance(results, schemas.MultiResults)
    assert assert_data(results, data)


def test_find_by_tvrage(get_data, assert_data):
    data = get_data("find/find")
    tvrage_id = "test"

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        results = tmdb.TMDb().find().by_tvrage(tvrage_id)
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/find/{tvrage_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "external_source": "tvrage_id",
            },
        )

    assert isinstance(results, schemas.MultiResults)
    assert assert_data(results, data)


def test_find_by_facebook(get_data, assert_data):
    data = get_data("find/find")
    facebook_id = "test"

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        results = tmdb.TMDb().find().by_facebook(facebook_id)
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/find/{facebook_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "external_source": "facebook_id",
            },
        )

    assert isinstance(results, schemas.MultiResults)
    assert assert_data(results, data)


def test_find_by_instagram(get_data, assert_data):
    data = get_data("find/find")
    instagram_id = "test"

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        results = tmdb.TMDb().find().by_instagram(instagram_id)
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/find/{instagram_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "external_source": "instagram_id",
            },
        )

    assert isinstance(results, schemas.MultiResults)
    assert assert_data(results, data)


def test_find_by_twitter(get_data, assert_data):
    data = get_data("find/find")
    twitter_id = "test"

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        results = tmdb.TMDb().find().by_twitter(twitter_id)
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/find/{twitter_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "external_source": "twitter_id",
            },
        )

    assert isinstance(results, schemas.MultiResults)
    assert assert_data(results, data)
