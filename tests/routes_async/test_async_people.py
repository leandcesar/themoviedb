# -*- coding: utf-8 -*-
from unittest.mock import patch

import pytest

from themoviedb import aiotmdb, schemas


@pytest.mark.asyncio
async def test_person_details(get_data, assert_data):
    data = get_data("people/details")
    person_id = 123

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        person = await aiotmdb.aioTMDb().person(person_id).details()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/person/{person_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "include_image_language": "null",
            },
        )

    assert isinstance(person, schemas.Person)
    assert assert_data(person, data)


@pytest.mark.asyncio
async def test_person_details_full(get_data, assert_data):
    data = get_data("people/details_full")
    data.pop("changes")  # TODO
    person_id = 123

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        person = (
            await aiotmdb.aioTMDb()
            .person(person_id)
            .details(
                append_to_response="changes,movie_credits,tv_credits,combined_credits,external_ids,images,tagged_images,translations"
            )
        )
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/person/{person_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "include_image_language": "null",
                "append_to_response": "changes,movie_credits,tv_credits,combined_credits,external_ids,images,tagged_images,translations",  # noqa: E501
            },
        )

    assert isinstance(person, schemas.Person)
    assert assert_data(person, data)


@pytest.mark.asyncio
async def test_person_external_ids(get_data, assert_data):
    data = get_data("people/external_ids")
    person_id = 123

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        external_ids = await aiotmdb.aioTMDb().person(person_id).external_ids()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/person/{person_id}/external_ids",
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
async def test_person_images(get_data, assert_data):
    data = get_data("people/images")
    person_id = 123

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        images = await aiotmdb.aioTMDb().person(person_id).images()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/person/{person_id}/images",
            params={
                "api_key": "TEST_TMDB_KEY",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(images, schemas.Images)
    assert assert_data(images, data)


@pytest.mark.asyncio
async def test_person_combined_credits(get_data, assert_data):
    data = get_data("people/combined_credits")
    person_id = 123

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        combined_credits = await aiotmdb.aioTMDb().person(person_id).combined_credits()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/person/{person_id}/combined_credits",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(combined_credits, schemas.CreditsCombined)
    assert assert_data(combined_credits, data)


@pytest.mark.asyncio
async def test_person_movie_credits(get_data, assert_data):
    data = get_data("people/movie_credits")
    person_id = 123

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        movie_credits = await aiotmdb.aioTMDb().person(person_id).movie_credits()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/person/{person_id}/movie_credits",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(movie_credits, schemas.CreditsMovie)
    assert assert_data(movie_credits, data)


@pytest.mark.asyncio
async def test_person_tv_credits(get_data, assert_data):
    data = get_data("people/tv_credits")
    person_id = 123

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        tv_credits = await aiotmdb.aioTMDb().person(person_id).tv_credits()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/person/{person_id}/tv_credits",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(tv_credits, schemas.CreditsTV)
    assert assert_data(tv_credits, data)


@pytest.mark.asyncio
async def test_person_tagged_images(get_data, assert_data):
    data = get_data("people/tagged_images")
    person_id = 123

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        tagged_images = await aiotmdb.aioTMDb().person(person_id).tagged_images()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/person/{person_id}/tagged_images",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(tagged_images, schemas.TaggedImages)
    assert assert_data(tagged_images, data)


@pytest.mark.asyncio
async def test_person_translations(get_data, assert_data):
    data = get_data("people/translations")
    person_id = 123

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        translations = await aiotmdb.aioTMDb().person(person_id).translations()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/person/{person_id}/translations",
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
async def test_people_latest(get_data, assert_data):
    data = get_data("people/latest")

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        person = await aiotmdb.aioTMDb().people().latest()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/person/latest",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(person, schemas.Person)
    assert assert_data(person, data)


@pytest.mark.asyncio
async def test_people_popular(get_data, assert_data):
    data = get_data("people/popular")

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        people = await aiotmdb.aioTMDb().people().popular()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/person/popular",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
            },
        )

    assert isinstance(people, schemas.People)
    assert assert_data(people, data)
