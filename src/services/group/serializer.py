"""Group Serializer"""
from typing import Optional, List

from pydantic import BaseModel
from pydantic.types import conlist, conint


class GroupInbound(BaseModel):
    """group inbound"""
    group_name: str
    user_ids: conlist(item_type=int, min_items=2, unique_items=True)
    owner_id: conint(gt=0)
    expense_name: Optional[str]
    comment: Optional[str]


class GroupOutbound(BaseModel):
    """group outbound"""
    id: int
    group_name: str
    user_ids: conlist(item_type=int, min_items=2, unique_items=True)
    owner_id: conint(gt=0)
    expense_name: Optional[str]
    comment: Optional[str]
    meta_data: Optional[dict]


class GroupFinalOutbound(BaseModel):
    """final outbound"""
    data: Optional[GroupOutbound]


class GroupListSingleOutbound(BaseModel):
    """Group list outbound"""
    id: int
    group_name: str
    user_ids: List[int]
    owner_id: int
    expense_name: Optional[str]
    comment: Optional[str]
    meta_data: Optional[dict]


class GroupListFinalOutbound(BaseModel):
    """Group list final outbound"""
    data: Optional[List[GroupListSingleOutbound]]
