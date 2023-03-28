from unittest.mock import patch

import pytest

from themoviedb import tmdb, schemas


def test_guest_rated_movies(get_data, assert_data):
    data = get_data("guest_sessions/rated_movies")
    guest_session_id = "SESSION_ID"

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        rated_movies = tmdb.TMDb().guest(guest_session_id).rated_movies()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/guest_session/{guest_session_id}/rated/movies",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(rated_movies, schemas.RatedMovies)
    assert assert_data(rated_movies, data)


def test_guest_rated_tvs(get_data, assert_data):
    data = get_data("guest_sessions/rated_tv_shows")
    guest_session_id = "SESSION_ID"

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        rated_tvs = tmdb.TMDb().guest(guest_session_id).rated_tvs()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/guest_session/{guest_session_id}/rated/tv",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(rated_tvs, schemas.RatedTVs)
    assert assert_data(rated_tvs, data)


def test_guest_rated_episodes(get_data, assert_data):
    data = get_data("guest_sessions/rated_tv_episodes")
    guest_session_id = "SESSION_ID"

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        rated_episodes = tmdb.TMDb().guest(guest_session_id).rated_episodes()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/guest_session/{guest_session_id}/rated/episodes",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(rated_episodes, schemas.RatedEpisodes)
    assert assert_data(rated_episodes, data)
