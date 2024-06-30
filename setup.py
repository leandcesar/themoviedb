#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.rst", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

requirements = [
    "aiohttp==3.9.5",
    "aiosignal==1.3.1",
    "async-timeout==4.0.2",
    "attrs==23.2.0",
    "certifi==2024.6.2",
    "charset-normalizer==3.3.2",
    "dacite==1.8.1",
    "frozenlist==1.4.1",
    "idna==3.7",
    "multidict==6.0.5",
    "requests==2.32.3",
    "urllib3==2.2.2",
    "yarl==1.9.4",
]

test_requirements = [
    "pytest",
    "pytest-asyncio",
]

setup(
    name="themoviedb",
    description="A modern and easy to use API wrapper for The Movie Database (TMDb) API v3 written in Python",
    long_description=readme,
    author="Leandro César",
    author_email="ccleandroc@gmail.com",
    url="https://github.com/leandcesar/themoviedb",
    version="0.4.0",
    license="MIT",
    python_requires=">=3.7",
    packages=find_packages(include=["themoviedb", "themoviedb.*"]),
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords=[
        "tmdb",
        "tmdb3",
        "aiotmdb",
        "aiotmdb3",
        "themoviedb",
        "themoviedb3",
        "sync",
        "async",
        "await",
        "aio",
        "movie",
        "movies",
        "tv",
        "tv show",
        "tv shows",
        "api",
        "wrapper",
    ],
    zip_safe=False,
    install_requires=requirements,
    tests_require=test_requirements,
    test_suite="tests",
)
