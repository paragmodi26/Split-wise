"""User Serializer"""
from typing import Optional, List

from pydantic import BaseModel
from pydantic.types import conlist, conint


class RelativeInbound(BaseModel):
    """relative amount"""
    user_id: int
    member_count: int


class AmountSplitInbound(BaseModel):
    """amount split inbound"""
    group_id: conint(gt=0)
    user_id: conint(gt=0)
    amount: float
    relative_meta: Optional[List[RelativeInbound]]


class AmountSplitOutbound(BaseModel):
    """Amount Split Outbound"""
    group_id: int
    user_id: int
    amount: float
    relative_meta: Optional[List[dict]]


class AmountSplitFinalOutbound(BaseModel):
    """Amount Split Final Outbound"""
    data: Optional[AmountSplitOutbound]
