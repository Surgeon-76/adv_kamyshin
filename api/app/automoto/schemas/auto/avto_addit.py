from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseAvtoAddit(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    power_steering: str = Field(description='Усилитель руля',
                                default='Электрический')
    climate: str = Field(description='Климатическая система',
                         default='Кондиционер')
    multirul: bool = Field(description='Управление на руле',
                           default=False)
    athermal_glass: bool = Field(description='Атермальное остекление',
                                 default=False)
    salon: str = Field(description='Отделка салона',
                       default='Ткань')
    leather_steering: bool = Field(description='Кожаный руль',
                                   default=False)
    sunfoof: bool = Field(description='Люк на крыше',
                          default=False)
    collor_salon: str = Field(description='Цвет салона',
                              default='Светлый')
    heat_front: bool = Field(description='Обогрев передних сидений',
                             default=False)
    heat_rear: bool = Field(description='Обогрев задних сидений',
                            default=False)
    heat_mirror: bool = Field(description='Обогрев зеркал',
                              default=False)
    heat_steering: bool = Field(description='Обогрев руля',
                                default=False)
    memory_front: bool = Field(description='Память настроек передних сидений',
                               default=False)
    memory_rear: bool = Field(description='Память настроек задних сидений',
                              default=False)
    memory_mirror: bool = Field(description='Память настроек зеркал',
                                default=False)
    memory_steering: bool = Field(description='Память настроек руля',
                                  default=False)
    autoparking: bool = Field(description='Автоматический парковщик',
                              default=False)
    rain_sensor: bool = Field(description='Датчик дождя',
                              default=False)
    light_sensor: bool = Field(description='Датчик света',
                               default=False)
    rear_parking: bool = Field(description='Парктроник задний',
                               default=False)
    front_parking: bool = Field(description='Парктроник передний',
                                default=False)
    bsd: bool = Field(description='Система контроля слепых зон',
                      default=False)
    rearview: bool = Field(description='Камера заднего вида',
                           default=False)
    cruise: bool = Field(description='Круиз-контроль',
                         default=False)
    bc: bool = Field(description='Бортовой компьютер',
                     default=False)
    signaling: bool = Field(description='Сигнализация',
                            default=False)
    centrallock: bool = Field(description='Центральный замок',
                              default=False)
    immobilizer: bool = Field(description='Иммобилайзер',
                              default=False)
    satellite: bool = Field(description='Спутник',
                            default=False)
    gsm: bool = Field(description='GSM',
                      default=False)
    airbag_front: bool = Field(description='Фронтальные airbag',
                               default=False)
    airbag_leg: bool = Field(description='Коленные airbag',
                             default=False)
    airbag_blind: bool = Field(description='Шторки airbag',
                               default=False)
    airbag_side_front: bool = Field(description='Боковые передние airbag',
                                    default=False)
    airbag_side_rear: bool = Field(description='Боковые задние airbag',
                                   default=False)
    abs: bool = Field(description='Антиблокировочная система',
                      default=False)
    asr: bool = Field(
        description='Противопробуксовочная система(ASR, DTS, TCS, TRC)',
        default=False)
    esp: bool = Field(description='Система курсовой устойчивости',
                      default=False)
    ebd: bool = Field(description='Система распределения тормозных усилий',
                      default=False)
    eba: bool = Field(description='Система экстренного торможения',
                      default=False)
    adl: bool = Field(description='Система блокировки дифференциала',
                      default=False)
    pds: bool = Field(description='Система обнаружения пешеходов и препятствий',
                      default=False)
    disk: bool = Field(description='CD/DVD/Blu-ray',
                       default=False)
    mp3: bool = Field(description='MP3',
                      default=False)
    radio: bool = Field(description='Радио',
                        default=False)
    tv: bool = Field(description='TV',
                     default=False)
    video: bool = Field(description='Видео',
                        default=False)
    swcontrol: bool = Field(description='Управление на руле',
                            default=False)
    usb: bool = Field(description='USB',
                      default=False)
    bluetooth: bool = Field(description='Bluetooth',
                            default=False)
    gpsnavi: bool = Field(description='GPS-навигатор',
                          default=False)
    audiosystem: str = Field(description='Аудиосистема(количество колонок)',
                             default='2 колонки')
    sw: bool = Field(description='Сабвуфер',
                     default=False)
    light: str = Field(description='Тип ламп головного света',
                       default='Галогеновые')
    fog_lights: bool = Field(description='Противотуманные фары',
                             default=False)
    head_wash: bool = Field(description='Омыватели фар',
                            default=False)
    adapt_light: bool = Field(description='Адаптивное освещение',
                              default=False)
    wheel_disk: str = Field(description='Размер колесных дисков',
                            default='14"')
    winter_tires: bool = Field(description='Зимние диски в комплекте',
                               default=False)


class AvtoAdditID(BaseModel):
    id: int = Field(description='ID Доп. опций легковых авто',)


class AvtoAdditView(BaseAvtoAddit, AvtoAdditID):
    pass


class AvtoAdditCreate(BaseAvtoAddit):
    pass


class AvtoAdditUpdate(BaseAvtoAddit, AvtoAdditID):
    pass

# #############################################################


class AvtoAdditResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: AvtoAdditView | None = None


class AvtoAdditError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class AvtoAdditPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[AvtoAdditView] | None = None
    total: int
    page: int
    size: int
    pages: int


class AvtoAdditPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class AvtoAdditDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
   tth: 'AvtoTth' = relationship(back_populates='addit',
                                          uselist=False)

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
