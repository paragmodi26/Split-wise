""" MODEL file for amount split api, this fill contains all db query realted to user table """
from src.configs.env import get_settings
from src.services.amount_split.schema import AmountSplitSchema
from src.db.session import get_db, save_new_row, select_first, update_old_row

db = get_db()
config = get_settings()


class AmountSplitModel:
    """class to query amount split table schema"""

    @classmethod
    def create(cls, **kw):
        """method to save new user"""
        obj = AmountSplitSchema(**kw)
        save_new_row(obj)
        return obj

    @classmethod
    def patch(cls, _id: int, **kw):
        """method to Update user"""
        obj = db.query(AmountSplitSchema).filter(AmountSplitSchema.id == _id).first()
        for key, value in kw.items():
            setattr(obj, key, value)
        update_old_row(obj)
        return cls.get_by_id(_id=_id)

    @classmethod
    def get_by_id(cls, _id: int):
        """get user by id"""
        rows = db.query(AmountSplitSchema).filter(AmountSplitSchema.id == _id)
        rows = select_first(rows)
        return rows
