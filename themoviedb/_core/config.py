import os
from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class ClientConfig:
    """Mutable request configuration shared by a client and its resources."""

    key: Optional[str]
    language: str
    region: str
    host: str = "https://api.themoviedb.org"
    version: str = "3"
    timeout: Optional[float] = None

    @classmethod
    def from_values(
        cls,
        *,
        key: Optional[str] = None,
        language: Optional[str] = None,
        region: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> "ClientConfig":
        """Build configuration from explicit values and the legacy environment variables."""
        return cls(
            key=key if key is not None else os.environ.get("TMDB_KEY"),
            language=language if language is not None else os.environ.get("TMDB_LANGUAGE", "en-US"),
            region=region if region is not None else os.environ.get("TMDB_REGION", "US"),
            timeout=timeout,
        )

    @property
    def default_params(self) -> Dict[str, Any]:
        """Return TMDb parameters included in every request."""
        return {
            "api_key": self.key,
            "language": self.language,
            "region": self.region,
            "watch_region": self.region,
        }
