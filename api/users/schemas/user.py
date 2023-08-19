from typing import Optional

from pydantic import BaseModel


class CreateUser(BaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None
    password: str
    agreement: bool = False

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    first_name: str
    family: str
    last_name: str
    email: str
    phone: str
    password: str
    type_user: str
    pers_web_site: str
    niсkname: str
    about_me: str
    site: str
    avatar: str

    class Config:
        orm_mode = True


class UpdateUserPassword(BaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None
    password: str

    class Config:
        orm_mode = True
