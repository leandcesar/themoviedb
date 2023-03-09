from unittest.mock import patch

import pytest

from themoviedb import routes, schemas


@pytest.mark.asyncio
async def test_tv_details(get_data, assert_data):
    data = get_data("tv/details")
    tv_id = 123

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        tv = await routes.TV(tv_id).details()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(tv, schemas.TV)
    assert assert_data(tv, data)


@pytest.mark.skip
@pytest.mark.asyncio
async def test_tv_details_full(get_data, assert_data):
    data = get_data("tv/details_full")
    tv_id = 123

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        tv = await routes.TV(tv_id).details(append_to_response="alternative_titles,changes,credits,external_ids,images,keywords,lists,recommendations,release_dates,reviews,similar,translations,videos,watch/providers")
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "append_to_response": "alternative_titles,changes,credits,external_ids,images,keywords,lists,recommendations,release_dates,reviews,similar,translations,videos,watch/providers",
            },
        )

    assert isinstance(tv, schemas.TV)
    assert assert_data(tv, data)


@pytest.mark.asyncio
async def test_tv_aggregate_credits(get_data, assert_data):
    data = get_data("tv/aggregate_credits")
    tv_id = 123

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        aggregate_credits = await routes.TV(tv_id).aggregate_credits()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/aggregate_credits",
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
async def test_tv_alternative_titles(get_data, assert_data):
    data = get_data("tv/alternative_titles")
    tv_id = 123

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        alternative_titles = await routes.TV(tv_id).alternative_titles()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/alternative_titles",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(alternative_titles, schemas.AlternativeTitles)
    assert assert_data(alternative_titles, data)


@pytest.mark.asyncio
async def test_tv_credits(get_data, assert_data):
    data = get_data("tv/credits")
    tv_id = 123

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        credits = await routes.TV(tv_id).credits()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/credits",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(credits, schemas.Credits)
    assert assert_data(credits, data)


@pytest.mark.asyncio
async def test_tv_external_ids(get_data, assert_data):
    data = get_data("tv/external_ids")
    tv_id = 123

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        external_ids = await routes.TV(tv_id).external_ids()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/external_ids",
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
async def test_tv_images(get_data, assert_data):
    data = get_data("tv/images")
    tv_id = 123

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        images = await routes.TV(tv_id).images()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/images",
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
async def test_tv_keywords(get_data, assert_data):
    data = get_data("tv/keywords")
    tv_id = 123

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        keywords = await routes.TV(tv_id).keywords()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/keywords",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(keywords, schemas.Keywords)
    assert assert_data(keywords, data)


@pytest.mark.asyncio
async def test_tv_recommendations(get_data, assert_data):
    data = get_data("tv/recommendations")
    tv_id = 123

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        recommendations = await routes.TV(tv_id).recommendations()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/recommendations",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
            },
        )

    assert isinstance(recommendations, schemas.TVs)
    assert assert_data(recommendations, data)


@pytest.mark.asyncio
async def test_tv_reviews(get_data, assert_data):
    data = get_data("tv/reviews")
    tv_id = 123

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        reviews = await routes.TV(tv_id).reviews()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/reviews",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
            },
        )

    assert isinstance(reviews, schemas.Reviews)
    assert assert_data(reviews, data)


@pytest.mark.asyncio
async def test_tv_similar(get_data, assert_data):
    data = get_data("tv/similar")
    tv_id = 123

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        similar = await routes.TV(tv_id).similar()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/similar",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
            },
        )

    assert isinstance(similar, schemas.TVs)
    assert assert_data(similar, data)


@pytest.mark.asyncio
async def test_tv_translations(get_data, assert_data):
    data = get_data("tv/translations")
    tv_id = 123

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        translations = await routes.TV(tv_id).translations()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/translations",
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
async def test_tv_videos(get_data, assert_data):
    data = get_data("tv/videos")
    tv_id = 123

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        videos = await routes.TV(tv_id).videos()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/videos",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
            },
        )

    assert isinstance(videos, schemas.Videos)
    assert assert_data(videos, data)


@pytest.mark.asyncio
async def test_tv_watch_providers(get_data, assert_data):
    data = get_data("tv/watch_providers")
    tv_id = 123

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        watch_providers = await routes.TV(tv_id).watch_providers()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/watch/providers",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(watch_providers, schemas.WatchProviders)
    assert assert_data(watch_providers, data)


@pytest.mark.asyncio
async def test_tvs_latest(get_data, assert_data):
    data = get_data("tv/latest")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        tv = await routes.TVs().latest()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/latest",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
            },
        )

    assert isinstance(tv, schemas.TV)
    assert assert_data(tv, data)


@pytest.mark.asyncio
async def test_tvs_airing_today(get_data, assert_data):
    data = get_data("tv/airing_today")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        tvs = await routes.TVs().airing_today()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/airing_today",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
            },
        )

    assert isinstance(tvs, schemas.TVs)
    assert assert_data(tvs, data)


@pytest.mark.asyncio
async def test_tvs_on_the_air(get_data, assert_data):
    data = get_data("tv/on_the_air")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        tvs = await routes.TVs().on_the_air()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/on_the_air",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
            },
        )

    assert isinstance(tvs, schemas.TVs)
    assert assert_data(tvs, data)


@pytest.mark.asyncio
async def test_tvs_popular(get_data, assert_data):
    data = get_data("tv/popular")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        tvs = await routes.TVs().popular()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/popular",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
            },
        )

    assert isinstance(tvs, schemas.TVs)
    assert assert_data(tvs, data)


@pytest.mark.asyncio
async def test_tvs_top_rated(get_data, assert_data):
    data = get_data("tv/top_rated")

    with patch("themoviedb.routes.base.ClientSession.request") as mocked:
        mocked.return_value.__aenter__.return_value.json.return_value = data
        tvs = await routes.TVs().top_rated()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/top_rated",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "en-US",
                "region": "US",
                "watch_region": "US",
                "page": 1,
            },
        )

    assert isinstance(tvs, schemas.TVs)
    assert assert_data(tvs, data)
