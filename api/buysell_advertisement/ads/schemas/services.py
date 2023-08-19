from typing import Optional

from pydantic import BaseModel, validator

from services.slug import generate_slug


class CreateService(BaseModel):
    name: str
    price: int
    unit_of_dim: str
    slug: Optional[str] = ''

    class Config:
        orm_mode = True

    @validator('slug')
    def set_slug(cls, slug, values, **kwargs):
        if 'name' in values and slug == '':
            slug = generate_slug(values['name'])
        return slug


class UpdateService(CreateService):
    id: int
