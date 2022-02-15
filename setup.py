# -*- coding: utf-8 -*-
import os
import sys
from shutil import rmtree

from setuptools import Command, find_packages, setup

with open("README.rst", "rb") as f:
    long_description = f.read().decode("utf-8")

here = os.path.abspath(os.path.dirname(__file__))


class PublishCommand(Command):
    """Support setup.py publish."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds...")
            rmtree(os.path.join(here, "dist"))
        except Exception:
            pass

        self.status("Building Source and Wheel (universal) distribution...")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPi via Twine...")
        os.system("twine upload dist/*")

        sys.exit()


setup(
    name="tmdb-python",
    version="0.0.4",
    description="Asynchronous Python library for The Movie Database (TMDB) API v3",
    long_description=long_description,
    url="https://github.com/leandcesar/tmdb-python",
    author="Leandro César",
    author_email="ccleandroc@gmail.com",
    license="MIT",
    packages=find_packages(exclude=("tests",)),
    keywords=[
        "movie",
        "movies",
        "tv",
        "tv show",
        "tv shows",
        "tmdb",
        "themoviedb",
        "moviedb",
        "movie database",
        "api",
        "wrapper",
    ],
    install_requires=["aiohttp"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
    ],
    cmdclass={
        "publish": PublishCommand,
    },
    zip_safe=False,
)
