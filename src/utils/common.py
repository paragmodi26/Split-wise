"""Common utilities"""
from typing import List, Optional

from pydantic import BaseModel

from src.configs.constants import EmailConstant


class EmailInBound(BaseModel):
    """Email inbound"""
    to_addrs: List[str]
    from_addrs: str = EmailConstant.FROM_EMAIL
    cc: Optional[List[str]] = []
    bcc: Optional[List[str]] = []
    reply_to: Optional[str] = []
    subject: str
    body: Optional[str] = None
    body_html: Optional[str] = None

