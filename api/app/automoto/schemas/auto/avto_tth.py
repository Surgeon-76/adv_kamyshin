from datetime import date

from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseAvtoTth(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    body_id: int = Field(description='ID body_type')
    addit_id: int = Field(description='ID avto_addit')
    release_year: date = Field(description='Год выпуска',
                               default=date.today()
                                               .strftime("%YYYY"))
    doors: int = Field(description='Количество дверей',
                       default=4)
    generation: int | None = Field(description='Поколение',
                                   default=None)
    engine_type: str = Field(description='Тип двигателя',
                             default='Бензин')
    transmission: str = Field(description='Какой привод',
                              default='Передний')
    gearbox: str = Field(description='КПП',
                         default='Механическая')
    version: str | None = Field(
        description='Модификация(прим:1.6 МТ (125 л.с.))',
        default=None)
    package: str | None = Field(description='Комплектация',
                                default=None)
    wheel: str = Field(description='Руль', default='Правый')

# #TODO: определиться с типом release_year, м.б. использовать str с ограничением по длине?


class AvtoTthID(BaseModel):
    id: int = Field(description='ID Технических характеристик авто')


class AvtoTthView(BaseAvtoTth, AvtoTthID):
    pass


class AvtoTthCreate(BaseAvtoTth):
    pass


class AvtoTthUpdate(BaseAvtoTth, AvtoTthID):
    pass

# #############################################################


class AvtoTthResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: AvtoTthView | None = None


class AvtoTthError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class AvtoTthPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[AvtoTthView] | None = None
    total: int
    page: int
    size: int
    pages: int


class AvtoTthPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class AvtoTthDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    transport: 'Transport'] = relationship(back_populates='avto_tth',
                                                  uselist=False)
    addit: 'AvtoAddit'] = relationship(back_populates='tth')

    release_year  'Год выпуска'
    doors         'Количество дверей'
    generation    'Поколение'
    engine_type   'Тип двигателя(Бензин, Дизель, Газ, Гибрид, Электро)'
    transmission  'Привод: Задний, Передний, Полный'
    gearbox       'КПП: Механическая, Автоматическая, Вариатор,
                        Роботизированная, Прямой привод'
    version       'Модификация(1.6 МТ (125 л.с.))'
    package       'Комплектация: Базовая, Trend, Trend Sport, Titanium'
    wheel         'Руль: Правый, Левый'
"""
