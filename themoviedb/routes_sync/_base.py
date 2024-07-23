# -*- coding: utf-8 -*-
import os
from typing import Any, Dict, Optional

from requests import Session


class Base:
    TMDB_URL = "https://api.themoviedb.org"
    TMDB_VERSION = "3"

    def __init__(
        self,
        *,
        key: Optional[str] = None,
        session: Optional[Session] = None,
        language: Optional[str] = None,
        region: Optional[str] = None,
    ):
        self._key = key if key is not None else os.environ.get("TMDB_KEY")
        self._session = session
        self._language = language if language is not None else os.environ.get("TMDB_LANGUAGE", "en-US")
        self._region = region if region is not None else os.environ.get("TMDB_REGION", "US")

    @property
    def session(self) -> Optional[Session]:
        return self._session

    @session.setter
    def session(self, session: Session) -> None:
        self._session = session

    @property
    def key(self) -> Optional[str]:
        return self._key

    @key.setter
    def key(self, key: str) -> None:
        self._key = key

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
        return self.TMDB_URL

    @property
    def _version(self) -> str:
        return self.TMDB_VERSION

    @property
    def _params(self) -> Dict[str, Any]:
        return {
            "api_key": self.key,
            "language": self.language,
            "region": self.region,
            "watch_region": self.region,
        }

    def request(self, path: str, method: str = "GET", **kwargs) -> Dict[str, Any]:
        url = f"{self._host}/{self._version}/{path}"
        json = kwargs.pop("json", None)
        params = {k.replace("__", "."): v for k, v in kwargs.items() if v is not None}
        params = {**self._params, **params}

        if self.session is not None:
            if json is None:
                response = self.session.request(method, url, params=params)
            else:
                response = self.session.request(method, url, params=params, json=json)
            response.raise_for_status()
            data = response.json()
        else:
            with Session() as session:
                if json is None:
                    with session.request(method, url, params=params) as response:
                        response.raise_for_status()
                        data = response.json()
                else:
                    with session.request(method, url, params=params, json=json) as response:
                        response.raise_for_status()
                        data = response.json()

        if "watch/providers" in data:
            data["watch_providers"] = data.pop("watch/providers")
        return data
