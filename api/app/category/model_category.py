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


class Category(Base):
    __tablename__ = 'categorys'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String())

    realest: Mapped['RealEstate'
                    ] = relationship(back_populates='parcels')

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    space     'Площадь земельного участка'
"""
