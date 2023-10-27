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


class Photo(Base):
    __tablename__ = 'photo'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    ads_id: Mapped[int] = mapped_column(Integer, ForeignKey('ads.id',
                                                            ondelete='CASCADE'))
    url: Mapped[str] = mapped_column(String(), default='')
    # #TODO: Переделать в base64 url

    ads: Mapped['Ads'] = relationship(back_populates='photo')

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
   url 'url-путь изображения'
"""
