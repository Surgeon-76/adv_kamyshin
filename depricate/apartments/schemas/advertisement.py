import decimal

from pydantic import BaseModel


class ADSAppartCreate(BaseModel):
    title: str
    body: str
    rooms: str
    originality: str
    price: decimal.Decimal
    total: float
    living: float
    finish: str
    auxiliary: str
    sanitary: str
    buildingtype: str
    category: int
    address: int
    user: int

    class Config:
        orm_mode = True


class ADSAppartUpdate(ADSAppartCreate):
    id: int
    closed: bool
