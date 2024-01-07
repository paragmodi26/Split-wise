"""Group Controller"""
from src.configs.error_constants import ErrorMessage
from src.exceptions.errors.generic import EntityException
from src.services.group.model import GroupModel
from src.services.group.serializer import GroupInbound, GroupFinalOutbound, GroupOutbound, GroupListSingleOutbound, \
    GroupListFinalOutbound
from src.services.user.model import UserModel


class GroupController:
    """group controller"""

    @classmethod
    async def save(cls, payload: GroupInbound):
        """group save"""
        group = GroupModel.get_by_name(name=payload.group_name)
        if group:
            raise EntityException(message=ErrorMessage.RECORD_ALREADY_EXISTS.format("Group Name"))
        user_data = UserModel.get_user(ids=payload.user_ids)
        if not user_data:
            raise EntityException(message=ErrorMessage.INVALID_ID.format("User"))
        ids = [user.id for user in user_data]
        if set(payload.user_ids) - set(ids):
            raise EntityException(message=ErrorMessage.INVALID_ID.format("User"))
        data = GroupModel.create(**payload.dict())
        return GroupFinalOutbound(data=GroupOutbound(**data.__dict__))

    @classmethod
    async def get_list(cls):
        """get all groups"""
        data = GroupModel.get_all()
        data = [GroupListSingleOutbound(**item.__dict__) for item in data] if data else None
        return GroupListFinalOutbound(data=data)

    @classmethod
    async def delete(cls, _id: int, owner_id: int):
        """delete group"""
        data = GroupModel.get_by_id(_id=_id, owner_id=owner_id)
        if not data:
            raise EntityException(message=ErrorMessage.INVALID_ID.format("Group"))
        GroupModel.delete_by_id(_id=_id)
        return True
