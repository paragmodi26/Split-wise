"""
file to contain the env specific configs
"""
import os
from functools import lru_cache
from pydantic import BaseSettings


class DBConfig:
    """
    db config
    """
    db_name: str
    db_host: str
    db_username: str
    db_password: str


class AppDBConfig(DBConfig):
    """
    App Db config
    """

    db_host: str = os.getenv("DB_HOST", "localhost")
    db_name: str = os.getenv("DB_NAME", "splitwise")
    db_username: str = os.getenv("DB_USERNAME", "postgres")
    db_password: str = os.getenv("DB_PASSWORD", "postgress")


class BaseConfig(BaseSettings):
    """Base config"""

    env = os.getenv("APP_ENV", "local")
    db_app: DBConfig = AppDBConfig
    redis_port = os.getenv("BROKER_PORT", 6379)
    redis_host: str = os.getenv("BROKER_HOST", "localhost")
    redis_db: int = 13
    postmark_token: str = os.getenv("POSTMARK_TOKEN", "")


@lru_cache()
def get_settings():
    """
    get env
    """
    return BaseConfig()
