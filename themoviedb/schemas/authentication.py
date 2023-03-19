from datetime import datetime
from dataclasses import dataclass
from typing import Dict, List, Optional, Union


@dataclass
class Response:
    success: Optional[bool] = None


@dataclass
class Authentication(Response):
    expires_at: Optional[str] = None

    @property
    def valid_until(self) -> Optional[datetime]:
        try:
            return datetime.strptime(self.expires_at, "%Y-%m-%d %H:%M:%S UTC")
        except Exception as e:
            return None


@dataclass
class GuestAuthentication(Authentication):
    guest_session_id: Optional[str] = None


@dataclass
class TokenAuthentication(Authentication):
    request_token: Optional[str] = None


@dataclass
class Session(Response):
    session_id: Optional[str] = None
