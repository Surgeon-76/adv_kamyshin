from __future__ import annotations

import decimal

from sqlalchemy import (
    DECIMAL,
    Integer
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from config.database import Base


class Parcels(Base):
    __tablename__ = 'parcels'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    space: Mapped[decimal.Decimal
                  ] = mapped_column(DECIMAL(precision=10,
                                            scale=2),
                                    default=0.00)

    realest: Mapped['RealEstate'
                    ] = relationship(back_populates='parcels')

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    space     'Площадь земельного участка'
"""
