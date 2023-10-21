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


class ModelMoto(Base):
    __tablename__ = 'model_moto'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    brand_id: Mapped[int] = mapped_column(Integer, ForeignKey('brand_moto.id'))
    model: Mapped[str] = mapped_column(String())

    brand: Mapped['BrandMoto'] = relationship(back_populates='model')
    mototype: Mapped[list['MotoType']] = relationship(back_populates='model')

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    model 'Модель мото'
"""
