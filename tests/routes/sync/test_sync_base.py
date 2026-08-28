from themoviedb import TMDb


def test_tmdb_init_by_env():
    tmdb = TMDb()

    assert tmdb.api_key == "TEST_TMDB_API_KEY"
    assert tmdb.session is None
    assert tmdb.language == "TEST_TMDB_LANGUAGE"
    assert tmdb.region == "TEST_TMDB_REGION"


def test_tmdb_init_by_args():
    tmdb = TMDb(
        api_key="KEY_BY_ARG",
        session="SESSION_BY_ARG",
        language="LANGUAGE_BY_ARG",
        region="REGION_BY_ARG",
    )

    assert tmdb.api_key == "KEY_BY_ARG"
    assert tmdb.session == "SESSION_BY_ARG"
    assert tmdb.language == "LANGUAGE_BY_ARG"
    assert tmdb.region == "REGION_BY_ARG"


def test_tmdb_init_by_set():
    tmdb = TMDb()
    tmdb.api_key = "KEY_BY_SET"
    tmdb.session = "SESSION_BY_SET"
    tmdb.language = "LANGUAGE_BY_SET"
    tmdb.region = "REGION_BY_SET"

    assert tmdb.api_key == "KEY_BY_SET"
    assert tmdb.session == "SESSION_BY_SET"
    assert tmdb.language == "LANGUAGE_BY_SET"
    assert tmdb.region == "REGION_BY_SET"
