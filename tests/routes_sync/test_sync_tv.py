# -*- coding: utf-8 -*-
from unittest.mock import patch

from themoviedb import schemas, tmdb


def test_tv_details(get_data, assert_data):
    data = get_data("tv/details")
    tv_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        tv = tmdb.TMDb().tv(tv_id).details()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(tv, schemas.TV)
    assert assert_data(tv, data)


def test_tv_details_full(get_data, assert_data):
    data = get_data("tv/details_full")
    data.pop("changes")  # TODO
    tv_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        tv = (
            tmdb.TMDb()
            .tv(tv_id)
            .details(
                append_to_response="aggregate_credits,alternative_titles,changes,content_ratings,credits,external_ids,episode_groups,images,keywords,recommendations,reviews,screened_theatrically,similar,translations,videos,watch/providers"
            )
        )
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "append_to_response": "aggregate_credits,alternative_titles,changes,content_ratings,credits,external_ids,episode_groups,images,keywords,recommendations,reviews,screened_theatrically,similar,translations,videos,watch/providers",  # noqa: E501
            },
        )

    assert isinstance(tv, schemas.TV)
    assert assert_data(tv, data)


def test_tv_aggregate_credits(get_data, assert_data):
    data = get_data("tv/aggregate_credits")
    tv_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        aggregate_credits = tmdb.TMDb().tv(tv_id).aggregate_credits()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/aggregate_credits",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(aggregate_credits, schemas.Credits)
    assert assert_data(aggregate_credits, data)


def test_tv_alternative_titles(get_data, assert_data):
    data = get_data("tv/alternative_titles")
    tv_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        alternative_titles = tmdb.TMDb().tv(tv_id).alternative_titles()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/alternative_titles",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(alternative_titles, schemas.AlternativeTitles)
    assert assert_data(alternative_titles, data)


def test_tv_content_ratings(get_data, assert_data):
    data = get_data("tv/content_ratings")
    tv_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        content_ratings = tmdb.TMDb().tv(tv_id).content_ratings()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/content_ratings",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(content_ratings, schemas.ContentRatings)
    assert assert_data(content_ratings, data)


def test_tv_credits(get_data, assert_data):
    data = get_data("tv/credits")
    tv_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        credits_ = tmdb.TMDb().tv(tv_id).credits()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/credits",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(credits_, schemas.Credits)
    assert assert_data(credits_, data)


def test_tv_episode_groups(get_data, assert_data):
    data = get_data("tv/episode_groups")
    tv_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        episode_groups = tmdb.TMDb().tv(tv_id).episode_groups()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/episode_groups",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(episode_groups, schemas.EpisodeGroups)
    assert assert_data(episode_groups, data)


def test_tv_external_ids(get_data, assert_data):
    data = get_data("tv/external_ids")
    tv_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        external_ids = tmdb.TMDb().tv(tv_id).external_ids()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/external_ids",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(external_ids, schemas.ExternalIDs)
    assert assert_data(external_ids, data)


def test_tv_images(get_data, assert_data):
    data = get_data("tv/images")
    tv_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        images = tmdb.TMDb().tv(tv_id).images()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/images",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(images, schemas.Images)
    assert assert_data(images, data)


def test_tv_keywords(get_data, assert_data):
    data = get_data("tv/keywords")
    tv_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        keywords = tmdb.TMDb().tv(tv_id).keywords()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/keywords",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(keywords, schemas.Keywords)
    assert assert_data(keywords, data)


def test_tv_recommendations(get_data, assert_data):
    data = get_data("tv/recommendations")
    tv_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        recommendations = tmdb.TMDb().tv(tv_id).recommendations()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/recommendations",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
            },
        )

    assert isinstance(recommendations, schemas.TVs)
    assert assert_data(recommendations, data)


def test_tv_reviews(get_data, assert_data):
    data = get_data("tv/reviews")
    tv_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        reviews = tmdb.TMDb().tv(tv_id).reviews()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/reviews",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
            },
        )

    assert isinstance(reviews, schemas.Reviews)
    assert assert_data(reviews, data)


def test_tv_screened_theatrically(get_data, assert_data):
    data = get_data("tv/screened_theatrically")
    tv_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        screened_theatrically = tmdb.TMDb().tv(tv_id).screened_theatrically()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/screened_theatrically",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(screened_theatrically, schemas.Episodes)
    assert assert_data(screened_theatrically, data)


def test_tv_similar(get_data, assert_data):
    data = get_data("tv/similar")
    tv_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        similar = tmdb.TMDb().tv(tv_id).similar()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/similar",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
            },
        )

    assert isinstance(similar, schemas.TVs)
    assert assert_data(similar, data)


def test_tv_translations(get_data, assert_data):
    data = get_data("tv/translations")
    tv_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        translations = tmdb.TMDb().tv(tv_id).translations()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/translations",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(translations, schemas.Translations)
    assert assert_data(translations, data)


def test_tv_videos(get_data, assert_data):
    data = get_data("tv/videos")
    tv_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        videos = tmdb.TMDb().tv(tv_id).videos()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/videos",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
            },
        )

    assert isinstance(videos, schemas.Videos)
    assert assert_data(videos, data)


def test_tv_watch_providers(get_data, assert_data):
    data = get_data("tv/watch_providers")
    tv_id = 123

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        watch_providers = tmdb.TMDb().tv(tv_id).watch_providers()
        mocked.assert_called_with(
            "GET",
            f"https://api.themoviedb.org/3/tv/{tv_id}/watch/providers",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(watch_providers, schemas.WatchProviders)
    assert assert_data(watch_providers, data)


def test_tvs_latest(get_data, assert_data):
    data = get_data("tv/latest")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        tv = tmdb.TMDb().tvs().latest()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/tv/latest",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
            },
        )

    assert isinstance(tv, schemas.TV)
    assert assert_data(tv, data)


def test_tvs_airing_today(get_data, assert_data):
    data = get_data("tv/airing_today")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        tvs = tmdb.TMDb().tvs().airing_today()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/tv/airing_today",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
            },
        )

    assert isinstance(tvs, schemas.TVs)
    assert assert_data(tvs, data)


def test_tvs_on_the_air(get_data, assert_data):
    data = get_data("tv/on_the_air")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        tvs = tmdb.TMDb().tvs().on_the_air()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/tv/on_the_air",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
            },
        )

    assert isinstance(tvs, schemas.TVs)
    assert assert_data(tvs, data)


def test_tvs_popular(get_data, assert_data):
    data = get_data("tv/popular")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        tvs = tmdb.TMDb().tvs().popular()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/tv/popular",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
            },
        )

    assert isinstance(tvs, schemas.TVs)
    assert assert_data(tvs, data)


def test_tvs_top_rated(get_data, assert_data):
    data = get_data("tv/top_rated")

    with patch("themoviedb.routes_sync._base.Session.request") as mocked:
        mocked.return_value.__enter__.return_value.json.return_value = data
        tvs = tmdb.TMDb().tvs().top_rated()
        mocked.assert_called_with(
            "GET",
            "https://api.themoviedb.org/3/tv/top_rated",
            params={
                "api_key": "TEST_TMDB_KEY",
                "language": "TEST_TMDB_LANGUAGE",
                "region": "TEST_TMDB_REGION",
                "watch_region": "TEST_TMDB_REGION",
                "page": 1,
            },
        )

    assert isinstance(tvs, schemas.TVs)
    assert assert_data(tvs, data)
