from typing import (
    List,
    Optional,
    Dict
)
import enum
from datetime import datetime

from pydantic import BaseModel

from .services import CreateService, UpdateService
from buysell_advertisement.categories.schemas.category import GetCategories


class CreateADs(BaseModel):
    agreement: bool
    user: int
    phone: str
    title: str
    descriptions: str
    category: int
    service: List[CreateService]

    class Config:
        orm_mode = True


class UpdateADs(CreateADs):
    id: int
    service: List[UpdateService]


class GetAds(BaseModel):
    id: int


class AdsGet(BaseModel):
    id: int
    title: str
    slug: str
    agreement: bool
    count_views: int
    phone: str
    descriptions: str
    created_on: datetime = None
    updated_on: datetime = None
    logo: str
    category: Optional[GetCategories]
    service: List[Dict]

    class Config:
        orm_mode = True
        validate_assignment = True


class AdsGetOne(AdsGet):
    photo_galery: Optional[List[Dict]] = None


class GetInfoAdsPaginations(BaseModel):
    total: Optional[int] = None
    count: Optional[int] = None
    prev_page: Optional[int] = None
    next_page: Optional[int] = None
    results: Optional[List[AdsGet]] = []
    # results :Optional[List] = []

    class Config:
        orm_mode = True
        validate_assignment = True


class DateEnum(str, enum.Enum):
    new = 'new'
    bye = 'bye'
