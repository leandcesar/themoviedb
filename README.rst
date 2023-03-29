|Code Quality Score| |Code Grade| |Code Coverage| |PyPI Version| |Code style: black| |PyPI License|

themoviedb
==========

.. raw:: html

   <h1 align="center">
     <a href="https://github.com/leandcesar/themoviedb">
       <img src="https://github.com/leandcesar/themoviedb/blob/master/docs/assets/themoviedb.gif?raw=true" alt="themoviedb"/>
     </a>
   </h1>


A modern and easy to use API wrapper for The Movie Database (TMDb) API v3
written in Python. Supports sync and async requests!

Overview
========

The **themoviedb** is a synchronous and asynchronous wrapper, written in Python,
for The Movie Database (TMDb) API v3.

`The Movie Database (TMDb) <https://www.themoviedb.org>`__ is a
community built movie and TV database.

The `TMDb API <https://www.themoviedb.org/documentation/api>`__ service
is for those of you interested in using our movie, TV show or actor
images and/or data in your application.

A `TMDb user account <https://www.themoviedb.org/account/signup>`__ is
required to request an API key.

Getting started
===============

Requirements
------------

-  ``python`` (Python >=3.8)
-  ``pip`` (Python package manager)

Install
-------

The easiest way to install themoviedb is via ``pip``.

::

    pip install themoviedb

API Key
-------

You will need an API key to The Movie Database to access the API. To
obtain a key, follow these steps:

1. `Register <https://www.themoviedb.org/account/signup>`__ for and
   verify an account.
2. `Log <https://www.themoviedb.org/login>`__ into your account.
3. Select the `API section <https://www.themoviedb.org/settings/api>`__
   on left side of your account page.
4. Click on the link to generate a new API key and follow the
   instructions.

Usage
=====

Sync mode
---------

.. code:: python

    from themoviedb import TMDb

Async mode
----------

.. code:: python

    from themoviedb import aioTMDb

Configuration
-------------

Initialize a TMDb object and set your API Key, language and region.

.. code:: python

    tmdb = TMDb(key="YOUR_API_KEY", language="pt-BR", region="BR")
    # or: tmdb = aioTMDb(key="YOUR_API_KEY", language="pt-BR", region="BR")

Alternatively, set after initialize.

.. code:: python

    tmdb = TMDb()
    # or: tmdb = aioTMDb()
    tmdb.key = "YOUR_API_KEY"
    tmdb.language = "pt-BR"     # default: en-US
    tmdb.region = "BR"          # default: US

Alternatively too, you can export your API key, language and region
logger as an environment variable.

.. code:: bash

    $ export TMDB_KEY="YOUR_API_KEY"
    $ export TMDB_LANGUAGE="pt-BR"  # ISO 639-1
    $ export TMDB_REGION="BR"       # ISO-3166-1

And then you will no longer need to set your API key, language and region.

.. code:: python

    tmdb = TMDb()   # from env: TMDB_KEY="YOUR_API_KEY", TMDB_LANGUAGE="pt-BR", TMDB_REGION="BR"
    # or: tmdb = aioTMDb()

Examples
--------

Get the list of top rated movies (sync mode).

.. code:: py

    from themoviedb import TMDb

    tmdb = TMDb()
    movies = tmdb.movies().top_rated()
    for movie in movies:
        print(movie)

Get the list of popular TV shows (async mode).

.. code:: py

    import asyncio
    from themoviedb import aioTMDb

    async def main():
        tmdb = aioTMDb()
        movies = await tmdb.tvs().popular()
        for movie in movies:
            print(movie)

    asyncio.run(main())

Discover movies by different types of data.

.. code:: py

    from themoviedb import TMDb

    tmdb = TMDb()
    movies = tmdb.discover().movie(
        sort_by="vote_average.desc",
        primary_release_date__gte="1997-08-15",
        vote_count__gte=10000,
        vote_average__gte=6.0,
    )
    for movie in movies:
        print(movie)

Get the details of movie for a search.

.. code:: py

    import asyncio
    from themoviedb import aioTMDb

    async def main():
        tmdb = aioTMDb()
        movies = await tmdb.search().movies("fight club")
        movie_id = movies[0].id  # get first result
        movie = await tmdb.movie(movie_id).details(append_to_response="credits,external_ids,images,videos")
        print(movie.title, movie.year)
        print(movie.tagline)
        print(movie.poster_url)
        print(movie.external_ids.imdb_url)
        for person in movie.credits.cast:
            print(person.name, person.character)

    asyncio.run(main())

.. |Code Quality Score| image:: https://api.codiga.io/project/36067/score/svg
   :target: https://app.codiga.io/hub/project/36067/themoviedb
.. |Code Grade| image:: https://api.codiga.io/project/36067/status/svg
   :target: https://app.codiga.io/hub/project/36067/themoviedb
.. |Code Coverage| image:: https://codecov.io/gh/leandcesar/themoviedb/branch/master/graph/badge.svg?token=OOILIE0RTS 
   :target: https://codecov.io/gh/leandcesar/themoviedb
.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
.. |PyPI Version| image:: https://img.shields.io/pypi/v/themoviedb?color=blue
   :target: https://pypi.org/project/themoviedb/
.. |PyPI License| image:: https://img.shields.io/pypi/l/themoviedb.svg
   :target: https://img.shields.io/pypi/l/themoviedb.svg
