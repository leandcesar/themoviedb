|Code Quality Score| |Code Grade| |Code Coverage| |PyPI Version| |Code style: black| |PyPI License|

themoviedb
==========

A modern and easy to use API wrapper for The Movie Database (TMDb) API v3 written in Python.

-  `Overview <#overview>`__
-  `Getting started <#getting-started>`__
-  `Configuration <#configuration>`__

--------------

Overview
========

The **themoviedb** is an asynchronous wrapper, written in Python, for The
Movie Database (TMDb) API v3.

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

-  ``python`` (Python >=3.7)
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
-----

The first step is to initialize a TMDb object and set your API Key.

.. code:: py

    import asyncio
    from themoviedb import TMDb

    async def main():
        tmdb = TMDb(key="YOUR_API_KEY")
        movies = await tmdb.search().movies("fight club")
        for movie in movies:
            print(movie)

    asyncio.run(main())

Alternatively, you can export your API key as an environment variable.

.. code:: bash

    $ export TMDB_KEY="YOUR_API_KEY"

And then you will no longer need to set your API key.

.. code:: py

    import asyncio
    from themoviedb import TMDb

    async def main():
        # implicit env var: TMDB_KEY="YOUR_API_KEY"
        tmdb = TMDb()
        movies = await tmdb.movies().now_playing()
        for movie in movies:
            print(movie)

    asyncio.run(main())

Configuration
=============

Initialize a TMDb object and set your API Key, language and region.

.. code:: py

    tmdb = TMDb()
    tmdb.key = "YOUR_API_KEY"
    tmdb.language = "pt-BR"
    tmdb.region = "BR"
    tvs = await tmdb.tvs().on_the_air()

Alternatively, you can export your API key, language and region
logger as an environment variable.

.. code:: bash

    $ export TMDB_KEY="YOUR_API_KEY"
    $ export TMDB_LANGUAGE="pt-BR"  # ISO 639-1
    $ export TMDB_REGION="BR"  # ISO-3166-1

And then you will no longer need to set your API key, language and region.

.. code:: py

    # implicit env vars: TMDB_KEY="YOUR_API_KEY" TMDB_LANGUAGE="pt-BR" TMDB_REGION="BR"
    tmdb = TMDb()
    people = await tmdb.people().popular()

You also can set language and region on object instantiation.

.. code:: py

    # implicit env vars: TMDB_KEY="YOUR_API_KEY" TMDB_LANGUAGE="pt-BR" TMDB_REGION="BR"
    tmdb = TMDb(key="ANOTHER_API_KEY")
    tvs = await tmdb.tvs(language="en-US", region="US").popular()  # with en-US / US
    tvs = await tmdb.tvs().popular()  # with pt-BR / BR

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
