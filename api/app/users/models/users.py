from __future__ import annotations
from sqlalchemy import(
    Integer,
    String
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)


from config.database import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    google_id: Mapped[int] = mapped_column(Integer, nullable=True)
    yandex_id: Mapped[int] = mapped_column(Integer, nullable=True)
    telegram_id: Mapped[int] = mapped_column(Integer, nullable=True)
    vk_id: Mapped[int] = mapped_column(Integer, nullable=True)
    username: Mapped[str] = mapped_column(String, index=True)
    first_name: Mapped[str] = mapped_column(String, default='user')
    last_name: Mapped[str | None] = mapped_column(String, default=None)
    avatar: Mapped[str | None] = mapped_column(String, default=None)

    def __repr__(self) -> str:
        return f"{self.__dict__}"
