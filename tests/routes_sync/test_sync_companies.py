from unittest.mock import patch

import pytest

from themoviedb import tmdb, schemas


def test_company_details(get_data, assert_data):
    data = get_data("companies/details")
    company_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        company = tmdb.TMDb().company(company_id).details()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/company/{company_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(company, schemas.Company)
    assert assert_data(company, data)


def test_company_alternative_names(get_data, assert_data):
    data = get_data("companies/alternative_names")
    company_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        alternative_names = tmdb.TMDb().company(company_id).alternative_names()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/company/{company_id}/alternative_names",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(alternative_names, schemas.AlternativeNames)
    assert assert_data(alternative_names, data)


def test_company_images(get_data, assert_data):
    data = get_data("companies/images")
    company_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        images = tmdb.TMDb().company(company_id).images()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/company/{company_id}/images",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(images, schemas.Images)
    assert assert_data(images, data)
