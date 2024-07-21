# -*- coding: utf-8 -*-
from themoviedb import schemas, utils
from themoviedb.routes_sync._base import Base


class Network(Base):
    def __init__(self, network_id: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.network_id = network_id

    def details(self) -> schemas.Network:
        """Get the details of a network.

        See more: https://developers.themoviedb.org/3/networks/get-network-details
        """
        data = self.request(f"network/{self.network_id}")
        return utils.as_dataclass(schemas.Network, data)

    def alternative_names(self) -> schemas.AlternativeNames:
        """Get the alternative names of a network.

        See more: https://developers.themoviedb.org/3/networks/get-network-alternative-names
        """
        data = self.request(f"network/{self.network_id}/alternative_names")
        return utils.as_dataclass(schemas.AlternativeNames, data)

    def images(self) -> schemas.Images:
        """Get the TV network logos by id.

        See more: https://developers.themoviedb.org/3/networks/get-network-images
        """
        data = self.request(f"network/{self.network_id}/images")
        return utils.as_dataclass(schemas.Images, data)
