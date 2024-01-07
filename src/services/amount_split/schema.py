"""User Schema"""
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import BIGINT, SMALLINT, JSONB
from src.configs.db_constants import DBConfig, DBTables
from src.db.session import Base


class AmountSplitSchema(Base):
    """User model schema for performing CRUD operations"""

    __tablename__  = DBTables.AMOUNT_SPLIT
    __table_args__ = DBConfig.BASE_ARGS

    id              = Column(SMALLINT, primary_key=True)
    group_id        = Column(BIGINT, nullable=False)
    user_id         = Column(BIGINT, nullable=False)
    amount          = Column(BIGINT)
    relative_meta   = Column(JSONB, default=lambda: {})
    meta_data       = Column(JSONB, default=lambda: {})
