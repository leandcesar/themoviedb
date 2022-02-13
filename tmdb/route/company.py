# -*- coding: utf-8 -*-
from .base import Base


class Company(Base):
    async def details(self, company_id: int) -> dict:
        """Get a companies details by id.

        See more: https://developers.themoviedb.org/3/companies/get-company-details
        """
        return await self.request(f"company/{company_id}")

    async def alternative_names(self, company_id: int) -> dict:
        """Get the alternative names of a company.

        See more: https://developers.themoviedb.org/3/companies/get-company-alternative-names
        """
        return await self.request(f"company/{company_id}/alternative_names")

    async def images(self, company_id: int) -> dict:
        """Get a companies logos by id.

        See more: https://developers.themoviedb.org/3/companies/get-company-images
        """
        return await self.request(f"company/{company_id}/images")

    async def search(self, query: str, *, page: int = 1) -> dict:
        """Search for companies.

        See more: https://developers.themoviedb.org/3/search/search-companies
        """
        return await self.request("search/company", query=query, page=page)
