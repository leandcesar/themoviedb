import os
from typing import Optional

from aiohttp import ClientSession


class Base:
    _TMDB_URL = "https://api.themoviedb.org"
    _TMDB_VERSION = "3"

    def __init__(
        self,
        *,
        session: ClientSession = None,
        language: Optional[str] = None,
        region: Optional[str] = None,
    ):
        self._session = session
        self._language = language if language is not None else os.environ.get("TMDB_LANGUAGE", "en-US")
        self._region = region if region is not None else os.environ.get("TMDB_REGION", "US")

    @property
    def session(self) -> ClientSession:
        return self._session

    @session.setter
    def session(self, session: ClientSession) -> None:
        self._session = session

    @property
    def key(self) -> str:
        return os.environ.get("TMDB_KEY")

    @key.setter
    def key(self, key: str) -> None:
        os.environ["TMDB_KEY"] = key

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
    def _host(self) -> str:
        return self._TMDB_URL

    @property
    def _version(self) -> str:
        return self._TMDB_VERSION

    @property
    def _params(self) -> dict:
        return {
            "api_key": self.key,
            "language": self.language,
            "region": self.region,
            "watch_region": self.region,
        }

    async def request(self, path: str, method: str = "GET", **kwargs) -> dict:
        url = f"{self._host}/{self._version}/{path}"
        params = {
            k.replace("__", "."): "true" if v is True else "false" if v is False else v
            for k, v in kwargs.items()
            if v is not None
        }
        params = {**self._params, **params}

        if self._session:
            response = await self.session.request(method, url, params=params)
            data = await response.json()
        else:
            async with ClientSession(raise_for_status=True) as session:
                async with session.request(method, url, params=params) as response:
                    data = await response.json()

        if "watch/providers" in data:
            data["watch_providers"] = data.pop("watch/providers")
        return data
