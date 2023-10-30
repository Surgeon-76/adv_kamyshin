from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseTransport(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    ads_id: int = Field(description='--> ads.id')
    auto_id: int = Field(description='--> avto_tth.id')
    moto_id: int = Field(description='--> moto_tth.id')
    color: int = Field(description='Цвет',
                       default=0)
    vin: str = Field(description='VIN или номер кузова(рамы)',
                     default='Нет')


class TransportID(BaseModel):
    id: int = Field(description='ID транспортного средства')


class TransportView(BaseTransport, TransportID):
    pass


class TransportCreate(BaseTransport):
    pass


class TransportUpdate(BaseTransport, TransportID):
    pass

# #############################################################


class TransportResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: TransportView | None = None


class TransportError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class TransportPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[TransportView] | None = None
    total: int
    page: int
    size: int
    pages: int


class TransportPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class TransportDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    ads: apped['Ads'] = relationship(back_populates='transport',
                                      uselist=False)

    color 'Цвет'
    vin 'VIN или номер кузова(рамы)'
"""
