from datetime import date

from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseMotoTth(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    moto_id: int = Field(description='--> moto_type.id')
    addit_id: int = Field(description='--> moto_addit.id')
    release_year: date = Field(description='Год выпуска',
                               default=date.today().strftime("%YYYY"))
    engine_type: str = Field(description='Тип двигателя',
                             default='Бензин')
    power: int | None = Field(description='Мощность двигателя, л/с',
                              default=None)
    volume: int | None = Field(description='Объём двигателя, см*3',
                               default=None)
    fuel_supply: str = Field(description='Подача топлива',
                             default='Карбюратор')
    drive_type: str = Field(description='Привод',
                            default='Цепь')
    cycles: str = Field(description='Число тактов',
                        default='2')
    cylinders: int = Field(description='Число цилиндров',
                           default=1)
    gearbox: str = Field(description='КПП',
                         default='Механика')
    scheme: str | None = Field(description='Раположение цилиндров',
                               default=None)
    cooling: str = Field(description='Охлаждение',
                         default='Воздушное')


class MotoTthID(BaseModel):
    id: int = Field(description='ID технических характеристик мото')


class MotoTthView(BaseMotoTth, MotoTthID):
    pass


class MotoTthCreate(BaseMotoTth):
    pass


class MotoTthUpdate(BaseMotoTth, MotoTthID):
    pass

# #############################################################


class MotoTthResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: MotoTthView | None = None


class MotoTthError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class MotoTthPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[MotoTthView] | None = None
    total: int
    page: int
    size: int
    pages: int


class MotoTthPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class MotoTthDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    transport: Mappedы['Transport'] = relationship(back_populates='avto_tth',
                                                  uselist=False)
    addit: Mappedы['MotoAddit'] = relationship(back_populates='tth')


    release_year  'Год выпуска'
    engine_type   'Тип двигателя(Бензин, Электро)'
    power         'Мощность двигателя л/с'
    volume        'Объём двигателя см*3'
    fuel_supply   'Подача топлива: Карбюратор, Инжектор'
    drive_type    'Привод: Цепь, Ремень, Кардан'
    cycles        'Число тактов: 2, 4'
    cylinders     'Число цилиндров: 1-...-6'
    gearbox       'КПП: Механика, Автомат, Вариатор, Робот'
    scheme        'Раположение цилиндров: V-образное, Оппозитное, Рядное'
    cooling       'Охлаждение: Воздушное, Жидкостное'
"""
