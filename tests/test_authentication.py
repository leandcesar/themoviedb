from unittest.mock import patch

import pytest

from themoviedb import tmdb, schemas


@pytest.mark.asyncio
async def test_create_guest_session(get_data, assert_data):
    data = get_data("authentication/create_guest_session")

    with patch("themoviedb.routes._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        session = await tmdb.TMDb().authentication().create_guest_session()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/authentication/guest_session/new",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            }
        )

    assert isinstance(session, schemas.GuestAuthentication)
    assert assert_data(session, data)


@pytest.mark.asyncio
async def test_create_token(get_data, assert_data):
    data = get_data("authentication/create_token")

    with patch("themoviedb.routes._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        token = await tmdb.TMDb().authentication().create_token()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/authentication/token/new",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            }
        )

    assert isinstance(token, schemas.TokenAuthentication)
    assert assert_data(token, data)


@pytest.mark.asyncio
async def test_create_session(get_data, assert_data):
    data = get_data("authentication/create_session")
    request_token = "TOKEN"

    with patch("themoviedb.routes._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        session = await tmdb.TMDb().authentication().create_session(request_token)
        mocked.assert_called_with(
            "POST",
            "https://api.themoviedb.org/3/authentication/session/new",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
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

    with patch("themoviedb.routes._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        session = await tmdb.TMDb().authentication().create_session_with_login(
            username,
            password,
            request_token,
        )
        mocked.assert_called_with(
            "POST",
            "https://api.themoviedb.org/3/authentication/token/validate_with_login",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
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

    with patch("themoviedb.routes._base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        session = await tmdb.TMDb().authentication().delete_session(session_id)
        mocked.assert_called_with(
            "DELETE",
            "https://api.themoviedb.org/3/authentication/session",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
            json={"session_id": session_id},
        )

    assert isinstance(session, schemas.Response)
    assert assert_data(session, data)
