from typing import Optional

from pydantic import BaseModel


class AddressCreate(BaseModel):
    address: str
    microdistrict: Optional[str]
    street: str
    house_number: str
    apartment_number: Optional[str] = ''
    locality: Optional[str]
    lat_coords: str
    long_coords: str

    class Config:
        orm_mode = True


class AddressUpdate(AddressCreate):
    pass
