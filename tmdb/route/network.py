# -*- coding: utf-8 -*-
from .base import Base, Response


class Network(Base):
    async def details(self, network_id: int) -> Response:
        """Get the details of a network.

        See more: https://developers.themoviedb.org/3/networks/get-network-details
        """
        return await self.request(f"network/{network_id}")

    async def alternative_names(self, network_id: int) -> Response:
        """Get the alternative names of a network.

        See more: https://developers.themoviedb.org/3/networks/get-network-alternative-names
        """
        return await self.request(f"network/{network_id}/alternative_names")

    async def images(self, network_id: int) -> Response:
        """Get the TV network logos by id.

        See more: https://developers.themoviedb.org/3/networks/get-network-images
        """
        return await self.request(f"network/{network_id}/images")
