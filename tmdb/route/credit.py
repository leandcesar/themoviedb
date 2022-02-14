# -*- coding: utf-8 -*-
from .base import Base, Response


class Credit(Base):
    async def details(self, credit_id: int) -> Response:
        """Get a movie or TV credit details by id.

        See more: https://developers.themoviedb.org/3/credits/get-credit-details
        """
        return await self.request(f"credit/{credit_id}")
