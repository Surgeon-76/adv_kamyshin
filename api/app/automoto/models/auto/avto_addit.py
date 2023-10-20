from __future__ import annotations

from sqlalchemy import (
    Boolean,
    Integer,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from config.database import Base


class AvtoAddit(Base):
    __tablename__ = 'avto_addit'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    power_steering: Mapped[str] = mapped_column(String(),
                                                default='Электроусилитель')
    climate: Mapped[str] = mapped_column(String(), default='Климат-контроль')
    multirul: Mapped[bool] = mapped_column(Boolean, default=False)
    athermal_glass: Mapped[bool] = mapped_column(Boolean, default=False)
    salon: Mapped[str] = mapped_column(String(), default='Велюр')
    leather_steering: Mapped[bool] = mapped_column(Boolean, default=False)
    sunfoof: Mapped[bool] = mapped_column(Boolean, default=False)
    collor_salon: Mapped[str] = mapped_column(String(), default='Светлый')
    heat_front: Mapped[bool] = mapped_column(Boolean, default=False)
    heat_rear: Mapped[bool] = mapped_column(Boolean, default=False)
    heat_mirror: Mapped[bool] = mapped_column(Boolean, default=False)
    heat_steering: Mapped[bool] = mapped_column(Boolean, default=False)
    memory_front: Mapped[bool] = mapped_column(Boolean, default=False)
    memory_rear: Mapped[bool] = mapped_column(Boolean, default=False)
    memory_mirror: Mapped[bool] = mapped_column(Boolean, default=False)
    memory_steering: Mapped[bool] = mapped_column(Boolean, default=False)
    autoparking: Mapped[bool] = mapped_column(Boolean, default=False)
    rain_sensor: Mapped[bool] = mapped_column(Boolean, default=False)
    light_sensor: Mapped[bool] = mapped_column(Boolean, default=False)
    rear_parking: Mapped[bool] = mapped_column(Boolean, default=False)
    front_parking: Mapped[bool] = mapped_column(Boolean, default=False)
    bsd: Mapped[bool] = mapped_column(Boolean, default=False)
    rearview: Mapped[bool] = mapped_column(Boolean, default=False)
    cruise: Mapped[bool] = mapped_column(Boolean, default=False)
    bc: Mapped[bool] = mapped_column(Boolean, default=False)
    signaling: Mapped[bool] = mapped_column(Boolean, default=False)
    centrallock: Mapped[bool] = mapped_column(Boolean, default=False)
    immobilizer: Mapped[bool] = mapped_column(Boolean, default=False)
    satellite: Mapped[bool] = mapped_column(Boolean, default=False)
    gsm: Mapped[bool] = mapped_column(Boolean, default=False)
    airbag_front: Mapped[bool] = mapped_column(Boolean, default=False)
    airbag_leg: Mapped[bool] = mapped_column(Boolean, default=False)
    airbag_blind: Mapped[bool] = mapped_column(Boolean, default=False)
    airbag_side_front: Mapped[bool] = mapped_column(Boolean, default=False)
    airbag_side_rear: Mapped[bool] = mapped_column(Boolean, default=False)
    abs: Mapped[bool] = mapped_column(Boolean, default=False)
    asr: Mapped[bool] = mapped_column(Boolean, default=False)
    esp: Mapped[bool] = mapped_column(Boolean, default=False)
    ebd: Mapped[bool] = mapped_column(Boolean, default=False)
    eba: Mapped[bool] = mapped_column(Boolean, default=False)
    adl: Mapped[bool] = mapped_column(Boolean, default=False)
    pds: Mapped[bool] = mapped_column(Boolean, default=False)
    disk: Mapped[bool] = mapped_column(Boolean, default=False)
    mp3: Mapped[bool] = mapped_column(Boolean, default=False)
    radio: Mapped[bool] = mapped_column(Boolean, default=False)
    tv: Mapped[bool] = mapped_column(Boolean, default=False)
    video: Mapped[bool] = mapped_column(Boolean, default=False)
    swcontrol: Mapped[bool] = mapped_column(Boolean, default=False)
    usb: Mapped[bool] = mapped_column(Boolean, default=False)
    bluetooth: Mapped[bool] = mapped_column(Boolean, default=False)
    gpsnavi: Mapped[bool] = mapped_column(Boolean, default=False)
    audiosystem: Mapped[str] = mapped_column(String(), default='2 колонки')
    sw: Mapped[bool] = mapped_column(Boolean, default=False)
    light: Mapped[str] = mapped_column(String(), 'Галогеновые')
    fog_lights: Mapped[bool] = mapped_column(Boolean, default=False)
    head_wash: Mapped[bool] = mapped_column(Boolean, default=False)
    adapt_light: Mapped[bool] = mapped_column(Boolean, default=False)
    wheel_disk: Mapped[str] = mapped_column(String(), default='14"')
    winter_tires: Mapped[bool] = mapped_column(Boolean, default=False)

    tth: Mapped['AvtoTth'] = relationship(back_populates='addit',
                                          uselist=False)

    def __repr__(self) -> str:
        return f"{self.__dict__}"


"""
    ............
"""
