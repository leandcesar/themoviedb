from unittest.mock import patch

import pytest

from themoviedb import tmdb, schemas


@pytest.mark.asyncio
async def test_season_details(get_data, assert_data):
    data = get_data("tv_seasons/details")
    tv_id = 123
    season_id = 456

    with patch("themoviedb.routes._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        season = await tmdb.TMDb().season(tv_id, season_id).details()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(season, schemas.Season)
    assert assert_data(season, data)


@pytest.mark.skip
@pytest.mark.asyncio
async def test_season_details_full(get_data, assert_data):
    data = get_data("tv_seasons/details_full")
    tv_id = 123
    season_id = 456

    with patch("themoviedb.routes._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        season = await tmdb.TMDb().season(tv_id, season_id).details(append_to_response="alternative_titles,changes,credits,external_ids,images,keywords,lists,recommendations,release_dates,reviews,similar,translations,videos,watch/providers")
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "append_to_response": "alternative_titles,changes,credits,external_ids,images,keywords,lists,recommendations,release_dates,reviews,similar,translations,videos,watch/providers",
            },
        )

    assert isinstance(season, schemas.Season)
    assert assert_data(season, data)


@pytest.mark.asyncio
async def test_season_aggregate_credits(get_data, assert_data):
    data = get_data("tv_seasons/aggregate_credits")
    tv_id = 123
    season_id = 456

    with patch("themoviedb.routes._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        aggregate_credits = await tmdb.TMDb().season(tv_id, season_id).aggregate_credits()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_id}/aggregate_credits",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(aggregate_credits, schemas.Credits)
    assert assert_data(aggregate_credits, data)


@pytest.mark.asyncio
async def test_season_credits(get_data, assert_data):
    data = get_data("tv_seasons/credits")
    tv_id = 123
    season_id = 456

    with patch("themoviedb.routes._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        credits_ = await tmdb.TMDb().season(tv_id, season_id).credits()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_id}/credits",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(credits_, schemas.Credits)
    assert assert_data(credits_, data)


@pytest.mark.asyncio
async def test_season_external_ids(get_data, assert_data):
    data = get_data("tv_seasons/external_ids")
    tv_id = 123
    season_id = 456

    with patch("themoviedb.routes._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        external_ids = await tmdb.TMDb().season(tv_id, season_id).external_ids()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_id}/external_ids",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(external_ids, schemas.ExternalIDs)
    assert assert_data(external_ids, data)


@pytest.mark.asyncio
async def test_season_images(get_data, assert_data):
    data = get_data("tv_seasons/images")
    tv_id = 123
    season_id = 456

    with patch("themoviedb.routes._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        images = await tmdb.TMDb().season(tv_id, season_id).images()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_id}/images",
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
async def test_season_translations(get_data, assert_data):
    data = get_data("tv_seasons/translations")
    tv_id = 123
    season_id = 456

    with patch("themoviedb.routes._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        translations = await tmdb.TMDb().season(tv_id, season_id).translations()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_id}/translations",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(translations, schemas.Translations)
    assert assert_data(translations, data)


@pytest.mark.asyncio
async def test_season_videos(get_data, assert_data):
    data = get_data("tv_seasons/videos")
    tv_id = 123
    season_id = 456

    with patch("themoviedb.routes._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        videos = await tmdb.TMDb().season(tv_id, season_id).videos()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_id}/videos",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(videos, schemas.Videos)
    assert assert_data(videos, data)
