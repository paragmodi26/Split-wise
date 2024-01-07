"""Route for user"""
from fastapi import APIRouter, Request

from src.services.user.controller import UserController
from src.services.user.serializer import UserInbound

router = APIRouter()


@router.post("/")
async def create_user(request: Request, payload: UserInbound):
    """API for create and update User"""
    return await UserController.save(payload=payload)


@router.get("/")
async def get_all_user(request: Request):
    """API for get all users"""
    return await UserController.get_all_users()


@router.get("/{id}")
async def get_all_user(request: Request, id: int):
    """API for get user by id"""
    return await UserController.get_by_id(_id=id)

