# -*- coding: utf-8 -*-
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Response:
    success: Optional[bool] = None


@dataclass
class Authentication(Response):
    expires_at: Optional[str] = None

    @property
    def valid_until(self) -> Optional[datetime]:
        if self.expires_at is None:
            return None
        try:
            return datetime.strptime(self.expires_at, "%Y-%m-%d %H:%M:%S UTC")
        except Exception:
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
