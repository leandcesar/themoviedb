# -*- coding: utf-8 -*-
from .base import Base, Response


class Collection(Base):
    async def details(self, collection_id: int) -> Response:
        """Get collection details by id.

        See more: https://developers.themoviedb.org/3/collections/get-collection-details
        """
        return await self.request(f"collection/{collection_id}")

    async def images(self, collection_id: int) -> Response:
        """Get the images for a collection by id.

        See more: https://developers.themoviedb.org/3/collections/get-collection-images
        """
        return await self.request(f"collection/{collection_id}/images")

    async def translations(self, collection_id: int) -> Response:
        """Get the list translations for a collection by id.

        See more: https://developers.themoviedb.org/3/collections/get-collection-translations
        """
        return await self.request(f"collection/{collection_id}/translations")

    async def search(self, query: str, *, page: int = 1) -> Response:
        """Search for collections.

        See more: https://developers.themoviedb.org/3/search/search-collections
        """
        return await self.request("search/collection", query=query, page=page)
