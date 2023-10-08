from __future__ import annotations
from sqlalchemy import (
    Boolean,
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
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    google_id: Mapped[str | None] = mapped_column(String, default=None)
    yandex_id: Mapped[str | None] = mapped_column(String, default=None)
    telegram_id: Mapped[str | None] = mapped_column(String, default=None)
    vk_id: Mapped[str | None] = mapped_column(String, default=None)
    username: Mapped[str] = mapped_column(String, index=True)
    first_name: Mapped[str] = mapped_column(String, default='user')
    last_name: Mapped[str | None] = mapped_column(String, default=None)
    email: Mapped[str | None] = mapped_column(String, default=None)
    avatar: Mapped[str | None] = mapped_column(String, default=None)

    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    is_client: Mapped[bool] = mapped_column(Boolean, default=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    def __repr__(self) -> str:
        return f"{self.__dict__}"
