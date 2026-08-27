from themoviedb import schemas
from themoviedb._endpoints.misc import FIND
from themoviedb._routes.sync._base import Base


class Find(Base):
    def _find(self, external_id: str, source: str) -> schemas.MultiResults:
        return self._request_endpoint(FIND, path_params={"external_id": external_id}, external_source=source)

    def by_imdb(self, imdb_id: str) -> schemas.MultiResults:
        return self._find(imdb_id, "imdb_id")

    def by_tvdb(self, tvdb_id: str) -> schemas.MultiResults:
        return self._find(tvdb_id, "tvdb_id")

    def by_freebase_mid(self, freebase_mid: str) -> schemas.MultiResults:
        return self._find(freebase_mid, "freebase_mid")

    def by_freebase(self, freebase_id: str) -> schemas.MultiResults:
        return self._find(freebase_id, "freebase_id")

    def by_tvrage(self, tvrage_id: str) -> schemas.MultiResults:
        return self._find(tvrage_id, "tvrage_id")

    def by_facebook(self, facebook_id: str) -> schemas.MultiResults:
        return self._find(facebook_id, "facebook_id")

    def by_instagram(self, instagram_id: str) -> schemas.MultiResults:
        return self._find(instagram_id, "instagram_id")

    def by_twitter(self, twitter_id: str) -> schemas.MultiResults:
        return self._find(twitter_id, "twitter_id")
