from typing import (
    Optional,
    List
)

from pydantic import BaseModel, validator

from services.slug import generate_slug


class CreateUpdateCategory(BaseModel):
    name: str
    parent_category: Optional[int] = None
    slug: Optional[str] = ''
    popular: Optional[bool] = False
    logo: Optional[str] = None

    class Config:
        orm_mode = True
        validate_assignment = True

    @validator("parent_category")
    def set_name(cls, parent_category):
        if parent_category == 0:
            return None
        return parent_category

    @validator('slug')
    def set_slug(cls, slug, values, **kwargs):
        if 'name' in values and slug == '':
            slug = generate_slug(values['name'])
        return slug


class FirstParentCategory(BaseModel):
    id: int
    name: str
    slug: str

    class Config:
        orm_mode = True


class ParentCategory(BaseModel):
    id: int
    name: str
    slug: str
    parent_category: Optional[FirstParentCategory] = None

    class Config:
        orm_mode = True


class GetCategories(BaseModel):
    id: int
    slug: str
    name: str
    parent_category: Optional[ParentCategory] = None

    class Config:
        orm_mode = True


class GetCategoriesList(BaseModel):
    categories: Optional[List[GetCategories]] = []

    class Config:
        orm_mode = True
