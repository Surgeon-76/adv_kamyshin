from __future__ import annotations

import decimal

from sqlalchemy import (
    DECIMAL,
    Integer,
    String,
    Text,
    ForeignKey
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from config.database import Base


class Ads(Base):
    __tablename__ = 'ads'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[decimal.Decimal] = mapped_column(DECIMAL(
        precision=10,scale=2), default=0.00)
    deposit: Mapped[decimal.Decimal | None] = mapped_column(DECIMAL(
        precision=10, scale=2), default=None)
    address: Mapped[str] = mapped_column(String, default='Адрес')
    price_one: Mapped[str] = mapped_column(String, default='за единицу')
    status: Mapped[str] = mapped_column(String, default='Активный')

    user_id: Mapped[int] = mapped_column(Integer,
                                         ForeignKey('user.id',
                                                    ondelete='CASCADE'))
    category_id: Mapped[int] = mapped_column(Integer,
                                             ForeignKey('categorys.id'))

    def __repr__(self) -> str:
        return f"{self.__dict__}"
