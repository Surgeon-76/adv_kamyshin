from __future__ import annotations

from sqlalchemy import (
    Integer,
    String
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from config.database import Base


class BrandMoto(Base):
    __tablename__ = 'brand_moto'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    brand: Mapped[str] = mapped_column(String())
    logo: Mapped[str] = mapped_column(String())

    model: Mapped[list['ModelMoto']] = relationship(back_populates='brand')

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    model 'Бренд мото'
    logo 'Логотип'
"""
