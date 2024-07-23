# -*- coding: utf-8 -*-
from unittest.mock import patch

import pytest

from themoviedb import aiotmdb, schemas


@pytest.mark.asyncio
async def test_episode_details(get_data, assert_data):
    data = get_data("tv_episodes/details")
    tv_id = 123
    season_id = 456
    episode_id = 789

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        episode = await aiotmdb.aioTMDb().episode(tv_id, season_id, episode_id).details()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_id}/episode/{episode_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(episode, schemas.Episode)
    assert assert_data(episode, data)


@pytest.mark.skip
@pytest.mark.asyncio
async def test_episode_details_full(get_data, assert_data):
    data = get_data("tv_episodes/details_full")
    tv_id = 123
    season_id = 456
    episode_id = 789

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        episode = (
            await aiotmdb.aioTMDb()
            .episode(tv_id, season_id, episode_id)
            .details(
                append_to_response="alternative_titles,changes,credits,external_ids,images,keywords,lists,recommendations,release_dates,reviews,similar,translations,videos,watch/providers"
            )
        )
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_id}/episode/{episode_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "append_to_response": "alternative_titles,changes,credits,external_ids,images,keywords,lists,recommendations,release_dates,reviews,similar,translations,videos,watch/providers",  # noqa: E501
            },
        )

    assert isinstance(episode, schemas.Episode)
    assert assert_data(episode, data)


@pytest.mark.asyncio
async def test_episode_credits(get_data, assert_data):
    data = get_data("tv_episodes/credits")
    tv_id = 123
    season_id = 456
    episode_id = 789

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        credits_ = await aiotmdb.aioTMDb().episode(tv_id, season_id, episode_id).credits()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_id}/episode/{episode_id}/credits",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(credits_, schemas.Credits)
    assert assert_data(credits_, data)


@pytest.mark.asyncio
async def test_episode_external_ids(get_data, assert_data):
    data = get_data("tv_episodes/external_ids")
    tv_id = 123
    season_id = 456
    episode_id = 789

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        external_ids = await aiotmdb.aioTMDb().episode(tv_id, season_id, episode_id).external_ids()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_id}/episode/{episode_id}/external_ids",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(external_ids, schemas.ExternalIDs)
    assert assert_data(external_ids, data)


@pytest.mark.asyncio
async def test_episode_images(get_data, assert_data):
    data = get_data("tv_episodes/images")
    tv_id = 123
    season_id = 456
    episode_id = 789

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        images = await aiotmdb.aioTMDb().episode(tv_id, season_id, episode_id).images()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_id}/episode/{episode_id}/images",
            params={
                "api_key": "TEST_TMDB_KEY",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(images, schemas.Images)
    assert assert_data(images, data)


@pytest.mark.asyncio
async def test_episode_translations(get_data, assert_data):
    data = get_data("tv_episodes/translations")
    tv_id = 123
    season_id = 456
    episode_id = 789

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        translations = await aiotmdb.aioTMDb().episode(tv_id, season_id, episode_id).translations()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_id}/episode/{episode_id}/translations",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(translations, schemas.Translations)
    assert assert_data(translations, data)


@pytest.mark.asyncio
async def test_episode_videos(get_data, assert_data):
    data = get_data("tv_episodes/videos")
    tv_id = 123
    season_id = 456
    episode_id = 789

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        videos = await aiotmdb.aioTMDb().episode(tv_id, season_id, episode_id).videos()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/season/{season_id}/episode/{episode_id}/videos",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(videos, schemas.Videos)
    assert assert_data(videos, data)
