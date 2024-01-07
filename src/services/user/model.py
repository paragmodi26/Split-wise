""" MODEL file for user api, this fill contains all db query realted to user table """
from typing import List

from src.configs.constants import StatusConstant
from src.configs.env import get_settings
from src.services.user.schema import UserSchema
from src.db.session import get_db, save_new_row, select_first, update_old_row, select_all

db = get_db()
config = get_settings()


class UserModel:
    """class to query user table schema"""

    @classmethod
    def create(cls, **kw):
        """method to save new user"""
        obj = UserSchema(**kw)
        save_new_row(obj)
        return obj

    @classmethod
    def patch(cls, _id: int, **kw):
        """method to Update user"""
        obj = db.query(UserSchema).filter(UserSchema.id == _id).first()
        for key, value in kw.items():
            setattr(obj, key, value)
        update_old_row(obj)
        return cls.get_user(_id=_id)

    @classmethod
    def get_user(cls, _id: int = None, email: str = None, ids: List[int] = None):
        """get user by id"""
        rows = db.query(UserSchema).filter(UserSchema.status == StatusConstant.Active)
        if _id:
            rows = rows.filter(UserSchema.id == _id)
        if email:
            rows = rows.filter(UserSchema.email == email)
        if ids:
            rows = rows.filter(UserSchema.id.in_(ids))
        if not _id and not email:
            rows = select_all(rows)
        else:
            rows = select_first(rows)
        return rows
