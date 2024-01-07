"""Route for amount split"""
from fastapi import APIRouter, Request

from src.services.amount_split.controller import AmountSplitController
from src.services.amount_split.serializer import AmountSplitInbound

router = APIRouter()


@router.post("/save")
async def save(request: Request, payload: AmountSplitInbound):
    """
    API for save Amount Split by user
    payload :   group_id required
                user_id required
                amount: required
                relative_meta: Optional
    """
    return await AmountSplitController.save(payload=payload)
