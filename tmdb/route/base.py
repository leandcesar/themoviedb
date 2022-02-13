# -*- coding: utf-8 -*-
import os
from datetime import date
from typing import Any

import aiohttp
from dacite import Config, from_dict


class Response(dict):
    def to(self, class_type: Any) -> Any:
        return from_dict(data_class=class_type, data=self, config=Config(type_hooks={date: date.fromisoformat}))


class Base:
    TMDB_URL = "https://api.themoviedb.org"
    TMDB_VERSION = "3"
    TMDB_KEY = "TMDB_KEY"
    TMDB_LANGUAGE = "TMDB_LANGUAGE"
    TMDB_REGION = "TMDB_REGION"

    def __init__(
        self,
        *,
        session: aiohttp.ClientSession = None,
        language: str = None,
        region: str = None,
    ):
        self._session = session
        self._language = language if language is not None else os.environ.get(self.TMDB_LANGUAGE, "en-US")
        self._region = region if region is not None else os.environ.get(self.TMDB_REGION, "US")

    @property
    def host(self) -> str:
        return self.TMDB_URL

    @property
    def version(self) -> str:
        return self.TMDB_VERSION

    @property
    def key(self) -> str:
        return os.environ.get(self.TMDB_KEY)

    @key.setter
    def key(self, key: str) -> None:
        os.environ[self.TMDB_KEY] = key

    @property
    def language(self) -> str:
        return self._language

    @language.setter
    def language(self, language: str) -> None:
        self._language = language

    @property
    def region(self) -> str:
        return self._region

    @region.setter
    def region(self, region: str) -> None:
        self._region = region

    @property
    def default_params(self) -> dict:
        return {
            "api_key": self.key,
            "language": self.language,
            "region": self.region,
            "watch_region": self.region,
        }

    async def request(self, path: str, method: str = "GET", **kwargs) -> Response:
        session = self._session or aiohttp.ClientSession()
        url = f"{self.host}/{self.version}/{path}"
        params = {
            k.replace("__", "."): "true" if v is True else "false" if v is False else v
            for k, v in kwargs.items()
            if v is not None
        }
        params = {**self.default_params, **params}

        response = await session.request(method, url=url, params=params)
        if self._session is None:
            await session.close()
        if not response.ok:
            response.raise_for_status()
        result = await response.json()

        if "watch/providers" in result:
            result["watch_providers"] = result.pop("watch/providers")
        return Response(result)
