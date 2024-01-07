""" MODEL file for group api, this fill contains all db query realted to user table """
from src.configs.constants import StatusConstant
from src.configs.env import get_settings
from src.services.group.schema import GroupSchema
from src.db.session import get_db, save_new_row, select_all, select_first, update_old_row, delete

db = get_db()
config = get_settings()


class GroupModel:
    """class to query user table schema"""

    @classmethod
    def create(cls, **kw):
        """method to save new user"""
        obj = GroupSchema(**kw)
        save_new_row(obj)
        return obj

    @classmethod
    def patch(cls, _id: int, **kw):
        """method to Update user"""
        obj = db.query(GroupSchema).filter(GroupSchema.id == _id).first()
        for key, value in kw.items():
            setattr(obj, key, value)
        update_old_row(obj)
        return cls.get_by_id(_id=_id)

    @classmethod
    def get_by_id(cls, _id: int, owner_id: int = None):
        """get user by id"""
        rows = db.query(GroupSchema).filter(GroupSchema.id == _id, GroupSchema.status == StatusConstant.Active)
        if owner_id:
            rows = rows.filter(GroupSchema.owner_id == owner_id)
        rows = select_first(rows)
        return rows

    @classmethod
    def get_by_name(cls, name: str):
        """get by name"""
        rows = db.query(GroupSchema).filter(
            GroupSchema.group_name == name,
            GroupSchema.status == StatusConstant.Active
        )
        rows = select_first(rows)
        return rows

    @classmethod
    def delete_by_id(cls, _id: int):
        """delete"""
        rows = db.query(GroupSchema).filter(GroupSchema.id == _id)
        rows = delete(rows)
        return rows

    @classmethod
    def get_all(cls):
        """get all groups"""
        rows = db.query(GroupSchema).filter(GroupSchema.status == StatusConstant.Active)
        rows = select_all(rows)
        return rows
