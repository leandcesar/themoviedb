from dataclasses import dataclass
from typing import Generic, Type, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class Endpoint(Generic[T]):
    """Describe one TMDb endpoint and the schema it returns."""

    path_template: str
    response_type: Type[T]
    method: str = "GET"

    def path(self, **path_params: object) -> str:
        """Render the route path from its resource identifiers."""
        return self.path_template.format(**path_params)
