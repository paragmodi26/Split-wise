"""Global Constants"""

from src.configs.env import get_settings

config = get_settings()
APP_CONTEXT_PATH = "/splitwise/api"
APP_CONTEXT_PATH_v2 = "/splitwise-internal/api"
RESPONSE_HEADERS = {
    "X-XSS-Protection": "1; mode=block",
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "deny",
    "Strict-Transport-Security": "deny",
    "Content-Security-Policy": "script-src 'self'",
}

ExternalApiTIMEOUT = 25

class MasterContants:
    """Master Constants"""

    DEFAULT_TIME_ZONE = "UTC"
    DEFAULT_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
    DATETIME_FORMAT_WITHOUT_T = "%Y-%m-%d %H:%M:%S"
    DEFAULT_DATE_FORMAT = "%Y-%m-%d"


class StatusConstant:
    """status constant"""
    Active = 1


class EmailConstant:
    """email constant"""
    FROM_EMAIL = "Splitwise <justforhost26@gmail.com>"
