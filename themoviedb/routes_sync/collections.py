# -*- coding: utf-8 -*-
from themoviedb import schemas, utils
from themoviedb.routes_sync._base import Base


class Collection(Base):
    def __init__(self, collection_id: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.collection_id = collection_id

    def details(self) -> schemas.Collection:
        """Get collection details by id.

        See more: https://developers.themoviedb.org/3/collections/get-collection-details
        """
        data = self.request(f"collection/{self.collection_id}")
        return utils.as_dataclass(schemas.Collection, data)

    def images(self) -> schemas.Images:
        """Get the images for a collection by id.

        See more: https://developers.themoviedb.org/3/collections/get-collection-images
        """
        data = self.request(f"collection/{self.collection_id}/images")
        return utils.as_dataclass(schemas.Images, data)

    def translations(self) -> schemas.Translations:
        """Get the list translations for a collection by id.

        See more: https://developers.themoviedb.org/3/collections/get-collection-translations
        """
        data = self.request(f"collection/{self.collection_id}/translations")
        return utils.as_dataclass(schemas.Translations, data)
