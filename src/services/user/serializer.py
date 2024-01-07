"""User Serializer"""
from pydantic import BaseModel
from pydantic.types import constr


class UserInbound(BaseModel):
    """Serializer for User"""
    name: constr(min_length=1, max_length=250)
    email: constr(strip_whitespace=True, max_length=100, regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    mobile_number: constr(min_length=1, max_length=15)


class UserSingleOutBound(BaseModel):
    """Serializer for User"""
    id: int
    name: str
    email: str
    mobile_number: str


class UserDetailsOutBound(BaseModel):
    """Serializer for User"""
    id: int
    name: str
    email: str
    mobile_number: str
    meta_data: dict = {}


class UserFinalOutbound(BaseModel):
    """Serializer for User"""
    data: UserDetailsOutBound


class UserMultiFinalOutBound(BaseModel):
    """multi user list outbound"""
    data: list[UserSingleOutBound]
