from typing import Optional

from pydantic import (
    BaseModel,
    ConfigDict
)


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None


class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    email: str


class UserOutSystem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    email: str


class SystemUser(UserOut):
    password: Optional[str]


class TokenRefresh(BaseModel):
    refresh: str
