from themoviedb import schemas
from themoviedb._endpoints.misc import CERTIFICATIONS_MOVIE, CERTIFICATIONS_TV
from themoviedb._routes.async_._base import Base


class Certifications(Base):
    async def movie(self) -> schemas.Certifications:
        return await self._request_endpoint(CERTIFICATIONS_MOVIE)

    async def tv(self) -> schemas.Certifications:
        return await self._request_endpoint(CERTIFICATIONS_TV)
