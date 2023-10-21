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


class RealEstate(Base):
    __tablename__ = 'real_estate'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    ids_id: Mapped[int] = mapped_column(Integer, ForeignKey('ads.id',
                                                            ondelete='CASCADE'))
    commerce_id: Mapped[int | None
                        ] = mapped_column(Integer,
                                          ForeignKey('commerce_building.id',
                                                     ondelete='CASCADE'),
                                          nullable=True)
    construction_id: Mapped[int | None
                            ] = mapped_column(Integer,
                                              ForeignKey('construction.id',
                                                         ondelete='CASCADE'),
                                              nullable=True)
    garage_id: Mapped[int | None
                      ] = mapped_column(Integer,
                                        ForeignKey('garage.id',
                                                   ondelete='CASCADE'),
                                        nullable=True)
    parking_id: Mapped[int | None
                       ] = mapped_column(Integer,
                                         ForeignKey('parking_space.id',
                                                    ondelete='CASCADE'),
                                         nullable=True)
    parcels_id: Mapped[int | None
                       ] = mapped_column(Integer,
                                         ForeignKey('parcels.id',
                                                    ondelete='CASCADE'),
                                         nullable=True)
    rooms_id: Mapped[int | None
                     ] = mapped_column(Integer,
                                       ForeignKey('rooms.id',
                                                  ondelete='CASCADE'),
                                       nullable=True)
    apart_id: Mapped[int | None
                      ] = mapped_column(Integer,
                                        ForeignKey('apartment.id',
                                                   ondelete='CASCADE'),
                                        nullable=True)
    latitude: Mapped[str] = mapped_column(String(), default='00\'00000"')
    longitude: Mapped[str] = mapped_column(String(), default='00\'00000"')

    ads: Mapped['Ads'] = relationship(back_populates='realest',
                                      uselist=False)
    contacts: Mapped['Contacts'] = relationship(back_populates='realest',
                                                uselist=False)

    def __repr__(self) -> str:
        return f"{self.__dict__}"
