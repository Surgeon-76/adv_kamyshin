from decimal import Decimal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseRooms(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    term_id: int | None = Field(description='--> term_transaction.id')
    rules: int | None = Field(description='--> rules_of_sett.id')
    type: str | None = Field(description='Тип дома',
                             default=None)
    rooms: str | None = Field(description='Комнат в квартире',
                              default=None)
    level: int = Field(description='Этажей в доме',
                       default=1)
    room_space: Decimal | None = Field(description='Площадь комнаты, м*2',
                                       precision=10,
                                       scale=2,
                                       default=None)
    beds: str | None = Field(description='Количество кроватей',
                             default=None)
    sleep: str | None = Field(description='Количество спальных мест',
                              default=None)
    wifi: bool | None = Field(description='Wi-Fi',
                              default=None)
    tv: bool | None = Field(description='Телевизор',
                            default=None)
    plate: bool | None = Field(description='Плита',
                               default=None)
    microwave: bool | None = Field(description='Мироволновка',
                                   default=None)
    fridge: bool | None = Field(description='Холодильник',
                                default=None)
    washing: bool | None = Field(description='Стиральная машинка',
                                 default=None)
    fan: bool | None = Field(description='Фен',
                             default=None)
    iron: bool | None = Field(description='Утюг',
                              default=None)
    ac: bool | None = Field(description='Кондиционер/Сплит',
                            default=None)
    fireplace: bool | None = Field(description='Камин',
                                   default=None)
    balcony: bool | None = Field(description='Балкон/Лоджия',
                                 default=None)
    parking: bool | None = Field(description='Парковка',
                                 default=None)
    bedding: bool | None = Field(description='Постельное бельё',
                                 default=None)
    towels: bool | None = Field(description='Полотенца',
                                default=None)
    hygiene: bool | None = Field(description='Средства гигиены',
                                 default=None)


class RoomsID(BaseModel):
    id: int = Field(description='ID комнаты')


class RoomsView(BaseRooms, RoomsID):
    pass


class RoomsCreate(BaseRooms):
    pass


class RoomsUpdate(BaseRooms, RoomsID):
    pass

# #############################################################


class RoomsResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: RoomsView | None = None


class RoomsError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class RoomsPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[RoomsView] | None = None
    total: int
    page: int
    size: int
    pages: int


class RoomsPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class RoomsDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    realest: Mappeds['RealEstate'
                    ] = relationship(back_populates='rooms')

    type        'Тип дома: Кирпичный,
                           Панельный,
                           Блочный,
                           Монолитный,
                           Монолитно-кирпичный,
                           Деревянный'
    rooms       'Комнат в квартире: 1, ... , 9, > 9'
    level       'Этажей в доме'
    room_space  'Площадь комнаты, м*2'
    beds        'Количество кроватей: 1, ... , 8 и более'
    sleep       'Количество спальных мест: 1, ... , 16 и    более'
    wifi        'Wi-Fi'
    tv          'Телевизор'
    plate       'Плита'
    microwave   'Мироволновка'
    fridge      'Холодильник'
    washing     'Стиральная машинка'
    fan         'Фен'
    iron        'Утюг'
    ac          'Кондиционер/Сплит'
    fireplace   'Камин'
    balcony     'Балкон/Лоджия'
    parking     'Парковка'
    bedding     'Постельное бельё'
    towels      'Полотенца'
    hygiene     'Средства гигиены'
"""
