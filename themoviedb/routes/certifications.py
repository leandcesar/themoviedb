from themoviedb import schemas, utils
from themoviedb.routes._base import Base


class Certifications(Base):

    async def movie(self) -> schemas.Certifications:
        """Get an up to date list of the officially supported movie certifications on TMDB.

        See more: https://developers.themoviedb.org/3/certifications/get-movie-certifications
        """
        data = await self.request("certification/movie/list")
        return utils.as_dataclass(schemas.Certifications, data)

    async def tv(self) -> schemas.Certifications:
        """Get an up to date list of the officially supported TV show certifications on TMDB.

        See more: https://developers.themoviedb.org/3/certifications/get-tv-certifications
        """
        data = await self.request("certification/tv/list")
        return utils.as_dataclass(schemas.Certifications, data)
