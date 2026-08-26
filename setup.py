import os
from pathlib import Path

from setuptools import find_packages, setup

PROJECT_ROOT = Path(__file__).resolve().parent

readme = (PROJECT_ROOT / "README.rst").read_text(encoding="utf-8")
requirements = (PROJECT_ROOT / "requirements.txt").read_text(encoding="utf-8").splitlines()

setup(
    name="themoviedb",
    description="A modern and easy to use API wrapper for The Movie Database (TMDb) API v3 written in Python",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="Leandro César",
    author_email="ccleandroc@gmail.com",
    url="https://github.com/leandcesar/themoviedb",
    version=os.environ.get("THEMOVIEDB_VERSION", "0.0.0.dev0"),
    license="MIT",
    python_requires=">=3.8,<3.15",
    packages=find_packages(include=["themoviedb", "themoviedb.*"]),
    include_package_data=True,
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
    keywords=[
        "tmdb",
        "tmdb3",
        "aiotmdb",
        "aiotmdb3",
        "themoviedb",
        "themoviedb3",
        "movie",
        "movies",
        "tv",
        "tv show",
        "tv shows",
    ],
    zip_safe=False,
    install_requires=requirements,
)
