"""Definition of all model"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, UniqueConstraint, Index
from sqlalchemy.dialects.postgresql import (
    ARRAY,
    BIGINT,
    JSONB,
    SMALLINT,
    VARCHAR,
)

from src.configs.db_constants import DBConfig, DBTables

Base = declarative_base()

class UserModel(Base):
    """User Model"""

    __tablename__  = DBTables.USER
    __table_args__ = DBConfig.BASE_ARGS

    id                        = Column(BIGINT, primary_key=True)
    name                      = Column(VARCHAR(250), nullable=False)
    email                     = Column(VARCHAR(100), nullable=False)
    mobile_number             = Column(VARCHAR(100))
    status                    = Column(SMALLINT, nullable=False, default=1)
    meta_data                 = Column(JSONB, default=lambda: {})
    UniqueConstraint(email, name="user_auth_email_key")


class GroupModel(Base):
    """group model """

    __tablename__  = DBTables.GROUP
    __table_args__ = DBConfig.BASE_ARGS

    id          = Column(BIGINT, primary_key=True)
    group_name  = Column(VARCHAR(250), nullable=False)
    user_ids    = Column(ARRAY(BIGINT))
    status      = Column(SMALLINT, nullable=False, default=1)
    owner_id    = Column(BIGINT, nullable=False)
    expense_name= Column(VARCHAR(250), nullable=False, default="New Expense")
    comment     = Column(VARCHAR(500), nullable=False)
    meta_data   = Column(JSONB, default=lambda: {})


class AmountSplitModel(Base):
    """User Role Model"""

    __tablename__   = DBTables.AMOUNT_SPLIT
    __table_args__  = DBConfig.BASE_ARGS

    id              = Column(SMALLINT, primary_key=True)
    group_id        = Column(BIGINT, nullable=False)
    user_id         = Column(BIGINT, nullable=False)
    amount          = Column(BIGINT)
    relative_meta   = Column(JSONB, default=lambda: {})
    meta_data       = Column(JSONB, default=lambda: {})



### INDEXING! ###
Index(DBTables.USER + "_email" + "_key", UserModel.email, unique=False)
Index(DBTables.AMOUNT_SPLIT + "_group_id" + "_key", AmountSplitModel.group_id, unique=False)