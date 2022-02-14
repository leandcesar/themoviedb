# -*- coding: utf-8 -*-
from .base import Base, Response


class Find(Base):
    async def by_imdb(self, imdb_id: str) -> Response:
        """Search movies, TV shows and people by IMDb ID.

        See more: https://developers.themoviedb.org/3/find/find-by-id
        """
        return await self.request(f"find/{imdb_id}", external_source="imdb_id")

    async def by_tvdb(self, tvdb_id: str) -> Response:
        """Search movies, TV shows and people by TVDb ID.

        See more: https://developers.themoviedb.org/3/find/find-by-id
        """
        return await self.request(f"find/{tvdb_id}", external_source="tvdb_id")

    async def by_freebase_mid(self, freebase_mid: str) -> Response:
        """Search movies, TV shows and people by Freebase MID.

        See more: https://developers.themoviedb.org/3/find/find-by-id
        """
        return await self.request(f"find/{freebase_mid}", external_source="freebase_mid")

    async def by_freebase(self, freebase_id: str) -> Response:
        """Search movies, TV shows and people by Freebase ID.

        See more: https://developers.themoviedb.org/3/find/find-by-id
        """
        return await self.request(f"find/{freebase_id}", external_source="freebase_id")

    async def by_tvrage(self, tvrage_id: str) -> Response:
        """Search movies, TV shows and people by TVRage ID.

        See more: https://developers.themoviedb.org/3/find/find-by-id
        """
        return await self.request(f"find/{tvrage_id}", external_source="tvrage_id")

    async def by_facebook(self, facebook_id: str) -> Response:
        """Search movies, TV shows and people by Facebook ID.

        See more: https://developers.themoviedb.org/3/find/find-by-id
        """
        return await self.request(f"find/{facebook_id}", external_source="facebook_id")

    async def by_instagram(self, instagram_id: str) -> Response:
        """Search movies, TV shows and people by Instagram ID.

        See more: https://developers.themoviedb.org/3/find/find-by-id
        """
        return await self.request(f"find/{instagram_id}", external_source="instagram_id")

    async def by_twitter(self, twitter_id: str) -> Response:
        """Search movies, TV shows and people by Twitter ID.

        See more: https://developers.themoviedb.org/3/find/find-by-id
        """
        return await self.request(f"find/{twitter_id}", external_source="twitter_id")
