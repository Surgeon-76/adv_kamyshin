from typing import Optional

import ormar

from settings.db import (
    database,
    metadata
    )

"""
    id: int
    address: str                        Адрес полный, либо создателя(?)
    microdistrict: Optional[str]        Микрорайон
    street: str                         Улица
    house_number: str                   Номер дома
    apartment_number: Optional[str]     Номер квартиры
    locality: Optional[str]             Город
    lat_coords: str                     GLONASS координата
    long_coords: str                    GLONASS координата
"""


class Address(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True, index=True)
    address: str = ormar.String(max_length=1000)
    microdistrict: Optional[str] = ormar.String(max_length=255, default='')
    street: str = ormar.String(max_length=255, default='')
    house_number: str = ormar.String(max_length=6, default='')
    apartment_number: Optional[str] = ormar.String(max_length=4, default='')
    locality: Optional[str] = ormar.String(max_length=255, nullable=True)
    lat_coords: str = ormar.String(max_length=255, default='')
    long_coords: str = ormar.String(max_length=255, default='')
