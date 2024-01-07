"""Email"""
from src.utils.common import EmailInBound
from src.configs.env import get_settings
from postmarker.core import PostmarkClient

config = get_settings()


class Email:
    """Email"""

    @classmethod
    async def send_email(cls, payload: EmailInBound):
        """Send email"""
        try:
            if payload.to_addrs:
                postmark = PostmarkClient(server_token=config.postmark_token)
                postmark.emails.send(
                    From=payload.from_addrs,
                    To=payload.to_addrs,
                    Subject=payload.subject,
                    HtmlBody=payload.body_html,
                    Cc=payload.cc,
                    Bcc=payload.bcc
                )
                return True
        except Exception as err:
            return False
