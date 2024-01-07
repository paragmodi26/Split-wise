"""amount split Controller"""
import copy
from src.configs.error_constants import ErrorMessage
from src.exceptions.errors.generic import EntityException
from src.services.amount_split.model import AmountSplitModel
from src.services.amount_split.serializer import AmountSplitInbound, AmountSplitOutbound, AmountSplitFinalOutbound
from src.services.group.model import GroupModel
from src.services.user.model import UserModel
from src.tasks.split_calculation import split_amount_task_main


class AmountSplitController:
    """Amount Split Controller"""

    @classmethod
    async def save(cls, payload: AmountSplitInbound):
        """group save"""
        group_data = GroupModel.get_by_id(_id=payload.group_id)
        if not group_data:
            raise EntityException(message=ErrorMessage.INVALID_ID.format("Group"))
        if payload.user_id not in group_data.user_ids:
            raise EntityException(message=ErrorMessage.INVALID_ID.format("Group User"))
        user_data = UserModel.get_user(_id=payload.user_id)
        if not user_data:
            raise EntityException(message=ErrorMessage.INVALID_ID.format("User"))

        for relative in (payload.relative_meta or []):
            if relative.user_id not in (group_data.user_ids or []):
                raise EntityException(message=ErrorMessage.INVALID_ID.format("Relative User"))

        data = AmountSplitModel.create(**payload.dict())
        data = copy.deepcopy(data)
        split_amount_task_main.delay(id=data.id)
        data = AmountSplitOutbound(**data.__dict__)
        return AmountSplitFinalOutbound(data=data)
