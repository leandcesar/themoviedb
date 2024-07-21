# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing import Optional

from themoviedb.schemas._enums import MediaType


@dataclass
class ExternalIDs:
    id: Optional[int] = None
    facebook_id: Optional[str] = None
    freebase_id: Optional[str] = None
    freebase_mid: Optional[str] = None
    imdb_id: Optional[str] = None
    instagram_id: Optional[str] = None
    tvdb_id: Optional[int] = None
    tvrage_id: Optional[int] = None
    twitter_id: Optional[str] = None
    tiktok_id: Optional[str] = None
    youtube_id: Optional[str] = None
    wikidata_id: Optional[str] = None

    @property
    def imdb_url(self) -> Optional[str]:
        if self.imdb_id and self.imdb_id.startswith("nm"):
            return f"https://www.imdb.com/name/{self.imdb_id}"
        if self.imdb_id and self.imdb_id.startswith("tt"):
            return f"https://www.imdb.com/title/{self.imdb_id}"
        return None

    @property
    def facebook_url(self) -> Optional[str]:
        return f"https://facebook.com/{self.facebook_id}" if self.facebook_id else None

    @property
    def instagram_url(self) -> Optional[str]:
        return f"https://instagram.com/{self.instagram_id}" if self.instagram_id else None

    @property
    def twitter_url(self) -> Optional[str]:
        return f"https://twitter.com/{self.twitter_id}" if self.twitter_id else None

    @property
    def tiktok_url(self) -> Optional[str]:
        return f"https://www.tiktok.com/@{self.tiktok_id}" if self.tiktok_id else None

    @property
    def youtube_url(self) -> Optional[str]:
        return f"https://www.youtube.com/@{self.youtube_id}" if self.youtube_id else None

    @property
    def wikidata_url(self) -> Optional[str]:
        return f"https://www.wikidata.org/wiki/{self.wikidata_id}" if self.wikidata_id else None

    def freebase_url(self, media_type: MediaType) -> Optional[str]:
        raise NotImplementedError()

    def tvdb_url(self, media_type: MediaType) -> Optional[str]:
        raise NotImplementedError()

    def tvrage_url(self, media_type: MediaType) -> Optional[str]:
        raise NotImplementedError()
