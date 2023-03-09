from unittest.mock import patch

import pytest

from themoviedb import routes, schemas


@pytest.mark.asyncio
async def test_review_details(get_data, assert_data):
    data = get_data("reviews/details")
    review_id = 123

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        review = await routes.Review(review_id).details()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/review/{review_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(review, schemas.Review)
    assert assert_data(review, data)
