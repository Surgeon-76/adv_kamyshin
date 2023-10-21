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
                                                default='Электрический')
    climate: Mapped[str] = mapped_column(String(), default='Кондиционер')
    multirul: Mapped[bool] = mapped_column(Boolean, default=False)
    athermal_glass: Mapped[bool] = mapped_column(Boolean, default=False)
    salon: Mapped[str] = mapped_column(String(), default='Ткань')
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
    power_steering    'Усилитель руля: Гидравлический, Электрический,
                                       Электрогидравлический, нет'
    climate           'Кондиционер, Климат-контроль однозонный,
                       Климат-контроль многозонный, нет'
    multirul          'Управление на руле'
    athermal_glass    'Атермальное остекление'
    salon             'Отделка салона: Кожа, Ткань, Велюр,  Комбинированный'
    leather_steering  'Кожаный руль'
    sunroof           'Люк на крыше'
    collor_salon      'Цвет салона: Светлый, Темный, Цветной'
    heat_front        'Обогрев передних сидений'
    heat_rear         'Обогрев задних сидений'
    heat_mirror       'Обогрев зеркал'
    heat_steering     'Обогрев руля'
    memory_front      'Память настроек передних сидений'
    memory_rear       'Память настроек задних сидений'
    memory_mirror     'Память настроек зеркал'
    memory_steering   'Память настроек руля'
    autoparking       'Автоматический парковщик'
    rain_sensor       'Датчик дождя'
    light_sensor      'Датчик света'
    rear_parking      'Парктроник задний'
    front_parking     'Парктроник передний'
    bsd               'Система контроля слепых зон'
    rearview          'Камера заднего вида'
    cruise            'Круиз-контроль'
    bc                'Бортовой компьютер'
    signaling         'Сигнализация'
    centrallock       'Центральный замок'
    immobilizer       'Иммобилайзер'
    satellite         'Спутник'
    gsm               'GSM'
    airbag_front      'Фронтальные airbag'
    airbag_leg        'Коленные airbag'
    airbag_blind      'Шторки airbag'
    airbag_side_front 'Боковые передние airbag'
    airbag_side_rear  'Боковые задние airbag'
    abs               'Антиблокировочная система'
    asr               'Противопробуксовочная система(ASR, DTS, TCS, TRC)'
    esp               'Система курсовой устойчивости'
    ebd               'Система распределения тормозных усилий'
    eba               'Система экстренного торможения'
    edl               'Система блокировки дифференциала'
    pds               'Система обнаружения пешеходов и препятствий'
    disk              'CD/DVD/Blu-ray'
    mp3               'MP3'
    radio             'Радио'
    tv                'TV'
    video             'Видео'
    swcontrol         'Управление на руле'
    usb               'USB'
    bluetooth         'Bluetooth'
    gpsnavi           'GPS-навигатор'
    audiosystem       '2 колонки,
                        4 колонки,
                        6 колонок,
                        8+ колонок'
    sw                'Сабвуфер'
    light             'Галогеновые, Ксеноновые, Светодиодные'
    fog_lights        'Противотуманные фары'
    head_wash         'Омыватели фар'
    adapt_light       'Адаптивное освещение'
    wheel_disk        'Размер диска:
                                     7" - ... - 30"'
    winter_tires      'Зимние диски в комплекте'
"""
