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

    @property
    def facebook_url(self) -> Optional[str]:
        return f"https://facebook.com/{self.facebook_id}" if self.facebook_id else None

    @property
    def instagram_url(self) -> Optional[str]:
        return f"https://instagram.com/{self.instagram_id}" if self.instagram_id else None

    @property
    def twitter_url(self) -> Optional[str]:
        return f"https://twitter.com/{self.twitter_id}" if self.twitter_id else None

    def freebase_url(self, media_type: MediaType) -> Optional[str]:
        raise NotImplementedError()

    def imdb_url(self, media_type: MediaType) -> Optional[str]:
        if self.imdb_id and media_type == MediaType.person:
            return f"https://www.imdb.com/name/{self.imdb_id}"
        elif self.imdb_id and media_type == MediaType.movie:
            return f"https://www.imdb.com/title/{self.imdb_id}"
        elif self.imdb_id and media_type == MediaType.tv:
            return f"https://www.imdb.com/title/{self.imdb_id}"
        return None

    def tvdb_url(self, media_type: MediaType) -> Optional[str]:
        raise NotImplementedError()

    def tvrage_url(self, media_type: MediaType) -> Optional[str]:
        raise NotImplementedError()
