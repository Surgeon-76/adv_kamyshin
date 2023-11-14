from decimal import Decimal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseGarage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    type: str = Field(description='Тип гаража', default='Кирпичный')
    space: Decimal = Field(description='Площадь гаража',
                           max_digits=10,
                           decimal_places=2,
                           default=0.00)
    security: bool = Field(description='Охрана',
                           default=False)


class GarageID(BaseModel):
    id: int = Field(description='ID объявления')


class GarageView(BaseGarage, GarageID):
    pass


class GarageCreate(BaseGarage):
    pass


class GarageUpdate(BaseGarage, GarageID):
    pass

# #############################################################


class GarageResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: GarageView | None = None


class GarageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class GaragePage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[GarageView] | None = None
    total: int
    page: int
    size: int
    pages: int


class GaragePageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class GarageDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    realest: Mappeds['RealEstate'
                       ] = relationship(back_populates='garage')

    type      'Тип гаража: Железобетонный, Кирпичный, Металлический'
    space     'Площадь гаража'
    security  'Охрана: Да, Нет'
"""
