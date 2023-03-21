from unittest.mock import patch

import pytest

from themoviedb import tmdb, schemas


def test_credit_details(get_data, assert_data):
    data = get_data("credits/details")
    credit_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        credit = tmdb.TMDb().credit(credit_id).details()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/credit/{credit_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(credit, schemas.Credit)
    assert assert_data(credit, data)
