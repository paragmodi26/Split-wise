"""Route for group"""
from fastapi import APIRouter, Request
from fastapi import APIRouter, Request, Response, status
from src.services.group.controller import GroupController
from src.services.group.serializer import GroupInbound

router = APIRouter()


@router.get("/list")
async def get_list(request: Request):
    """API for save group"""
    return await GroupController.get_list()


@router.post("/save")
async def save(request: Request, payload: GroupInbound):
    """API for save group
    payload :
                group_name: required
                user_ids: required
                owner_id: required
                expense_name: Optional
                comment: Optional
    """
    return await GroupController.save(payload=payload)


@router.delete("/delete")
async def delete(request: Request, id: int, owner_id: int):
    """API for save group"""
    await GroupController.delete(_id=id, owner_id=owner_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
