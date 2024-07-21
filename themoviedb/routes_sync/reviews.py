# -*- coding: utf-8 -*-
from themoviedb import schemas, utils
from themoviedb.routes_sync._base import Base


class Review(Base):
    def __init__(self, review_id: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.review_id = review_id

    def details(self) -> schemas.Review:
        """Retrieve the details of a movie or TV show review.

        See more: https://developers.themoviedb.org/3/reviews/get-review-details
        """
        data = self.request(f"review/{self.review_id}")
        return utils.as_dataclass(schemas.Review, data)
