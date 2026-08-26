from themoviedb import schemas, utils
from themoviedb.routes_sync._base import Base


class Company(Base):
    def __init__(self, company_id: int, **kwargs) -> None:
        super().__init__(**kwargs)
        self.company_id = company_id

    def details(self) -> schemas.Company:
        """Get a companies details by id.

        See more: https://developers.themoviedb.org/3/companies/get-company-details
        """
        data = self.request(f"company/{self.company_id}")
        return utils.as_dataclass(schemas.Company, data)

    def alternative_names(self) -> schemas.AlternativeNames:
        """Get the alternative names of a company.

        See more: https://developers.themoviedb.org/3/companies/get-company-alternative_names
        """
        data = self.request(f"company/{self.company_id}/alternative_names")
        return utils.as_dataclass(schemas.AlternativeNames, data)

    def images(self) -> schemas.Images:
        """Get a companies logos by id.

        See more: https://developers.themoviedb.org/3/companies/get-company-images
        """
        data = self.request(f"company/{self.company_id}/images")
        return utils.as_dataclass(schemas.Images, data)
