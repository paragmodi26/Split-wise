"""Route for ping"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.tasks.split_calculation import split_amount_task

router = APIRouter()


@router.get("")
async def ping():
    """Ping"""
    await split_amount_task(_id=16)
    return JSONResponse(content={"service": "ok"}, status_code=200)
