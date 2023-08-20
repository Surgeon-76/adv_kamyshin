from typing import Optional

from pydantic import BaseModel


class CategorieCreate(BaseModel):
    transaction: Optional[str] = 'продать'
    type_housing: Optional[str] = 'жилая'
    daily: bool = False


class CategorieUpdate(BaseModel):
    transaction: Optional[str]
    type_housing: Optional[str]
    daily: bool
