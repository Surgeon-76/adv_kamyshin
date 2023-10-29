from decimal import Decimal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseAds(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str = Field(description='Название объявления')
    description: str = Field(description='Описание объявления')
    price: Decimal = Field(description='Цена',
                           max_digits=10,
                           decimal_places=2,
                           default=0.00)
    deposit: Decimal | None = Field(description='Депозит(при снятии/аренде)',
                                    max_digits=10,
                                    decimal_places=2,
                                    default=None)
    address: str = Field(description='Адрес',
                         default='Адрес')
    price_one: str = Field(
        description='единица измерения(за единицу, за кг и т.д)',
        default='за единицу')
    status: str = Field(description='Статус объявления',
                        default='Активный')
    user_id: int = Field(description='ID Пользователя')
    category_id: int = Field(description='ID Категории')


class AdsID(BaseModel):
    id: int = Field(description='ID объявления')


class AdsView(BaseAds, AdsID):
    pass


class AdsCreate(BaseAds):
    pass


class AdsUpdate(BaseAds, AdsID):
    pass

# #############################################################


class AdsResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: AdsView | None = None


class AdsError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class AdsPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[AdsView] | None = None
    total: int
    page: int
    size: int
    pages: int


class AdsPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class AdsDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


# #TODO: relationship

"""
    transport: Mapped['Transport' | None] = relationship(back_populates='ads')
    realestate: Mapped['RealEstate' | None
                       ] = relationship(back_populates='ads')
    category: Mapped['Category'] = relationship(back_populates='ads')
"""
