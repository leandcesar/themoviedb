import os
import pytest

from themoviedb import aioTMDb


def test_aiotmdb_init_by_env():
    tmdb = aioTMDb()

    assert tmdb.key == "TEST_TMDB_KEY"
    assert tmdb.session is None
    assert tmdb.language == "TEST_TMDB_LANGUAGE"
    assert tmdb.region == "TEST_TMDB_REGION"
    assert tmdb.movies().key == "TEST_TMDB_KEY"
    assert tmdb.movies().session is None
    assert tmdb.movies().language == "TEST_TMDB_LANGUAGE"
    assert tmdb.movies().region == "TEST_TMDB_REGION"


def test_aiotmdb_init_by_args():
    tmdb = aioTMDb(
        key="KEY_BY_ARG",
        session="SESSION_BY_ARG",
        language="LANGUAGE_BY_ARG",
        region="REGION_BY_ARG",
    )

    assert tmdb.key == "KEY_BY_ARG"
    assert tmdb.session == "SESSION_BY_ARG"
    assert tmdb.language == "LANGUAGE_BY_ARG"
    assert tmdb.region == "REGION_BY_ARG"
    assert tmdb.movies().key == "KEY_BY_ARG"
    assert tmdb.movies().session == "SESSION_BY_ARG"
    assert tmdb.movies().language == "LANGUAGE_BY_ARG"
    assert tmdb.movies().region == "REGION_BY_ARG"


def test_aiotmdb_init_by_set():
    tmdb = aioTMDb()
    tmdb.key = "KEY_BY_SET"
    tmdb.session = "SESSION_BY_SET"
    tmdb.language = "LANGUAGE_BY_SET"
    tmdb.region = "REGION_BY_SET"

    assert tmdb.key == "KEY_BY_SET"
    assert tmdb.session == "SESSION_BY_SET"
    assert tmdb.language == "LANGUAGE_BY_SET"
    assert tmdb.region == "REGION_BY_SET"
    assert tmdb.movies().key == "KEY_BY_SET"
    assert tmdb.movies().session == "SESSION_BY_SET"
    assert tmdb.movies().language == "LANGUAGE_BY_SET"
    assert tmdb.movies().region == "REGION_BY_SET"
