from __future__ import annotations

from sqlalchemy import (
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from config.database import Base


class Category(Base):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    parent_id: Mapped[int] = mapped_column(Integer, ForeignKey('category.id'))
    title: Mapped[str] = mapped_column(String())

    children: Mapped['Category'
                     ] = relationship(back_populates='parent',
                                      cascade="all, delete-orphan",)
    parent: Mapped['Category' | None
                   ] = relationship(back_populates='children',
                                    remote_side=[id])

    ads: Mapped[list['Ads']] = relationship(back_populates='category')

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    title     'Наименование категории'
"""
