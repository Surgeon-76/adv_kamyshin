from typing import Optional

from pydantic import BaseModel

from ..users.models.manager import Role


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None


class UserOut(BaseModel):
    email: str

    class Config:
        orm_mode = True


class UserOutSystem(BaseModel):
    email: str
    role: Role | str = 'client'

    class Config:
        orm_mode = True


class SystemUser(UserOut):
    password: Optional[str]


class TokenRefresh(BaseModel):
    refresh: str
