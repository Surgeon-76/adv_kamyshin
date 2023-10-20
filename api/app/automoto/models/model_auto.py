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


class ModelAuto(Base):
    __tablename__ = 'model_auto'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    brand_id: Mapped[int] = mapped_column(Integer, ForeignKey('brand_auto.id'))
    model: Mapped[str] = mapped_column(String())

    body: Mapped[list['BodyType']] = relationship(back_populates='model')
    branb: Mapped['ModelAuto'] = relationship(back_populates='model')

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    model 'Модель авто'
"""
