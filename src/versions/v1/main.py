"""main file contains all the routes for the api"""
from fastapi import APIRouter
from src.versions.v1.routes import user, group, amount_split

api_router = APIRouter()

api_router.include_router(amount_split.router, prefix="/v1/amount-split", tags=["Amount Split"])
api_router.include_router(group.router, prefix="/v1/group", tags=["Group"])
api_router.include_router(user.router, prefix="/v1/user", tags=["User"])
