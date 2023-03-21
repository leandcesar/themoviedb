from themoviedb import schemas, utils
from themoviedb.routes_async._base import Base


class Credit(Base):
    def __init__(self, credit_id: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.credit_id = credit_id

    async def details(self) -> schemas.Credit:
        """Get a movie or TV credit details by id.

        See more: https://developers.themoviedb.org/3/credits/get-credit-details
        """
        data = await self.request(f"credit/{self.credit_id}")
        return utils.as_dataclass(schemas.Credit, data)
