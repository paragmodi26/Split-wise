"""User Controller"""
from src.configs.error_constants import ErrorMessage
from src.exceptions.errors.generic import EntityException
from src.services.user.model import UserModel
from src.services.user.serializer import (
    UserInbound, UserSingleOutBound, UserFinalOutbound, UserMultiFinalOutBound, UserDetailsOutBound
)


class UserController:
    """User controller for performing CRUD operations"""

    @classmethod
    async def save(cls, payload: UserInbound):
        """Save user"""
        user_exists = UserModel.get_user(email=payload.email)
        if user_exists:
            raise EntityException(message=ErrorMessage.RECORD_ALREADY_EXISTS.format("User"))
        user = UserModel.create(**payload.dict())
        return await cls.get_by_id(_id=user.id)

    @classmethod
    async def get_by_id(cls, _id: int):
        """Get user by id"""
        user = UserModel.get_user(_id=_id)
        if not user:
            raise EntityException(message=ErrorMessage.RECORD_NOT_FOUND)
        return UserFinalOutbound(data=UserDetailsOutBound(**user.__dict__))

    @classmethod
    async def get_all_users(cls):
        """Get all users"""
        users = UserModel.get_user()
        response = [UserSingleOutBound(**user.__dict__) for user in users] if users else []
        return UserMultiFinalOutBound(data=response)

