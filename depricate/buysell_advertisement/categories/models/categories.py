from typing import ForwardRef, Optional

import ormar

from settings.db import (
    database,
    metadata
)


CategoryRef = ForwardRef("Category")


class Category(ormar.Model):
    class Meta:
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=50, unique=True,)
    slug: str = ormar.String(max_length=255, unique=True, index=True)
    popular: bool = ormar.Boolean(default=False)
    logo: Optional[str] = ormar.String(max_length=255,nullable=True)

    parent_category: Optional[CategoryRef] = ormar.ForeignKey(
        CategoryRef,
        related_name="child_categories",
        nullable=True
        )

    class Config:
        orm_mode = True


Category.update_forward_refs()
