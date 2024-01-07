"""User Group Schema"""
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR, SMALLINT, JSONB, ARRAY
from src.configs.db_constants import DBConfig, DBTables
from src.db.session import Base


class GroupSchema(Base):
    """User Group model schema for performing CRUD operations"""

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
