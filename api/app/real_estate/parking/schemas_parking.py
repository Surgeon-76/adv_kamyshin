from decimal import Decimal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseParkingSpace(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    type: str = Field(description='Тип машино места',
                      default='Открытая стоянка')
    space: Decimal = Field(description='Площадь машино места',
                           max_digits=10,
                           decimal_places=2,
                           default=0.00)
    security: bool = Field(description='Охрана',
                           default=False)


class ParkingSpaceID(BaseModel):
    id: int = Field(description='ID машино места')


class ParkingSpaceView(BaseParkingSpace, ParkingSpaceID):
    pass


class ParkingSpaceCreate(BaseParkingSpace):
    pass


class ParkingSpaceUpdate(BaseParkingSpace, ParkingSpaceID):
    pass

# #############################################################


class ParkingSpaceResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: ParkingSpaceView | None = None


class ParkingSpaceError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class ParkingSpacePage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[ParkingSpaceView] | None = None
    total: int
    page: int
    size: int
    pages: int


class ParkingSpacePageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class ParkingSpaceDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    realest: Mappeds['RealEstate'
                       ] = relationship(back_populates='parking_space')

    type      'Тип машино места: Многоуровневый паркинг,
                                 Подземный паркинг,
                                 Крытая стоянка,
                                 Открытая стоянка'
    space     'Площадь машино места'
    security  'Охрана: Да, Нет'
"""
