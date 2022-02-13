# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional


@dataclass
class ExternalIDs:
    facebook_id: Optional[str]
    freebase_id: Optional[str]
    freebase_mid: Optional[str]
    imdb_id: Optional[str]
    instagram_id: Optional[str]
    tvdb_id: Optional[int]
    tvrage_id: Optional[str]
    twitter_id: Optional[str]

    @property
    def facebook(self) -> Optional[str]:
        if self.facebook_id:
            return f"https://facebook.com/{self.facebook_id}"

    def freebase(self, media_type: str) -> Optional[str]:
        raise NotImplementedError()

    @property
    def instagram(self) -> Optional[str]:
        if self.instagram_id:
            return f"https://instagram.com/{self.instagram_id}"

    def imdb(self, media_type: str) -> Optional[str]:
        if self.imdb_id and media_type == "person":
            return f"https://www.imdb.com/name/{self.imdb_id}"
        if self.imdb_id and media_type == "movie":
            return f"https://www.imdb.com/title/{self.imdb_id}"
        if self.imdb_id and media_type == "tv":
            return f"https://www.imdb.com/title/{self.imdb_id}"

    def tvdb(self, media_type: str) -> Optional[str]:
        raise NotImplementedError()

    def tvrage(self, media_type: str) -> Optional[str]:
        raise NotImplementedError()

    @property
    def twitter(self) -> Optional[str]:
        if self.twitter_id:
            return f"https://twitter.com/{self.twitter_id}"
