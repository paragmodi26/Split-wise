"""Database constants module"""


class DBTables:
    """Database tables class"""
    USER                   = "user"
    GROUP                  = "group"
    AMOUNT_SPLIT           = "amount_split"


class DBConfig:
    """Database configuration class"""
    SCHEMA_NAME = "splitwise"
    BASE_ARGS = {"schema": SCHEMA_NAME}
