from unittest.mock import patch

import pytest

from themoviedb import aiotmdb, schemas


@pytest.mark.asyncio
async def test_create_guest_session(get_data, assert_data):
    data = get_data("authentication/create_guest_session")

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        session = await aiotmdb.aioTMDb().authentication().create_guest_session()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/authentication/guest_session/new",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            }
        )

    assert isinstance(session, schemas.GuestAuthentication)
    assert assert_data(session, data)


@pytest.mark.asyncio
async def test_create_token(get_data, assert_data):
    data = get_data("authentication/create_token")

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        token = await aiotmdb.aioTMDb().authentication().create_token()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/authentication/token/new",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            }
        )

    assert isinstance(token, schemas.TokenAuthentication)
    assert assert_data(token, data)


@pytest.mark.asyncio
async def test_create_session(get_data, assert_data):
    data = get_data("authentication/create_session")
    request_token = "TOKEN"

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        session = await aiotmdb.aioTMDb().authentication().create_session(request_token)
        mocked.assert_called_with(
            "POST",
            "https://api.themoviedb.org/3/authentication/session/new",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
            json={"request_token": request_token},
        )

    assert isinstance(session, schemas.Session)
    assert assert_data(session, data)


@pytest.mark.asyncio
async def test_create_session_with_login(get_data, assert_data):
    data = get_data("authentication/create_session_with_login")
    username = "USERNAME"
    password = "PASSWORD"
    request_token = "TOKEN"

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        session = await aiotmdb.aioTMDb().authentication().create_session_with_login(
            username,
            password,
            request_token,
        )
        mocked.assert_called_with(
            "POST",
            "https://api.themoviedb.org/3/authentication/token/validate_with_login",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
            json={
                "username": username,
                "password": password,
                "request_token": request_token,
            },
        )

    assert isinstance(session, schemas.TokenAuthentication)
    assert assert_data(session, data)


@pytest.mark.asyncio
async def test_delete_session(get_data, assert_data):
    data = get_data("authentication/delete_session")
    session_id = "SESSION_ID"

    with patch("themoviedb.routes_async._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        session = await aiotmdb.aioTMDb().authentication().delete_session(session_id)
        mocked.assert_called_with(
            "DELETE",
            "https://api.themoviedb.org/3/authentication/session",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
            json={"session_id": session_id},
        )

    assert isinstance(session, schemas.Response)
    assert assert_data(session, data)
