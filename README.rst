|PyPI Version| |PyPI License| |Code style: black|

TMDb Python
===========

**tmdb-python**, an async Python library for TMDb API.

-  `Overview <#overview>`__
-  `Getting started <#getting-started>`__
-  `Configuration <#configuration>`__

--------------

Overview
========

The **tmdb-python** is an asynchronous wrapper, written in Python, for The
Movie Database (TMDb) API v3.

`The Movie Database (TMDB) <https://www.themoviedb.org>`__ is a
community built movie and TV database.

The `TMDB API <https://www.themoviedb.org/documentation/api>`__ service
is for those of you interested in using our movie, TV show or actor
images and/or data in your application.

A `TMDB user account <https://www.themoviedb.org/account/signup>`__ is
required to request an API key.

Getting started
===============

Requirements
------------

-  ``python`` (Python >=3.9)
-  ``pip`` (Python package manager)

Install
-------

The easiest way to install tmdb-python is via ``pip``.

::

    pip install tmdb-python

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

The first step is to initialize a TMDB object and set your API Key.

.. code:: py

    import asyncio
    from tmdb import route, schema

    async def main():
        base = route.Base()
        base.key = "YOUR_API_KEY"

        movies = await route.Movie().search("fight club")
        for movie in movies:
            print(movie["name"])

        movies = movies.to(schema.Movies)  # convert `dict` to `schema.Movies`
        for movie in movies:
            print(movie.name)

    asyncio.run(main())

Alternatively, you can export your API key as an environment variable.

.. code:: bash

    $ export TMDB_KEY="YOUR_API_KEY"

And then you will no longer need to set your API key.

.. code:: py

    import asyncio
    from tmdb import route

    async def main():
        # implicit env var: TMDB_KEY="YOUR_API_KEY"
        movies = await route.Movie().popular()
        for movie in movies:
            print(movie["name"])

    asyncio.run(main())

For more information, see the `docs <https://leandcesar.github.io/tmdb-python/>`__.

Configuration
=============

Initialize a TMDB object and set your API Key, language and region.

.. code:: py

    from tmdb import route

    async def main():
        base = route.Base()
        base.key = "YOUR_API_KEY"
        base.language = "pt-BR"
        base.region = "BR"

        providers = await route.Movie().providers_list()

Alternatively, you can export your API key, language and region
logger as an environment variable.

.. code:: bash

    $ export TMDB_KEY="YOUR_API_KEY"
    $ export TMDB_LANGUAGE="pt-BR"  # ISO 639-1
    $ export TMDB_REGION="BR"  # ISO-3166-1

And then you will no longer need to set your API key, language and region.

.. code:: py

    async def main():
        # implicit env vars: TMDB_KEY="YOUR_API_KEY" TMDB_LANGUAGE="pt-BR" TMDB_REGION="BR"
        providers = await route.Movie().providers_list()

You also can set language and region on object instantiation.

.. code:: py

    async def main():
        # implicit env vars: TMDB_KEY="YOUR_API_KEY" TMDB_LANGUAGE="pt-BR" TMDB_REGION="BR"
        movies = await route.Movie().discover()  # discover with the BR regional release date
        movies = await route.Movie(language="en-US", region="US").discover()  # discover with the US regional release date

.. |Code style: black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
.. |PyPI Version| image:: https://img.shields.io/pypi/v/tmdb-python?color=blue
   :target: https://pypi.org/project/tmdb-python/
.. |PyPI License| image:: https://img.shields.io/pypi/l/tmdb-python.svg
   :target: https://img.shields.io/pypi/l/tmdb-python.svg
