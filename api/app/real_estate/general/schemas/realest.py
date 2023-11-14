from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseRealEstate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    ids_id: int = Field(description='--> ads.id')
    commerce_id: int | None = Field(description='--> commerce_building.id',
                                    default=None)
    construction_id: int | None = Field(description='--> construction.id',
                                        default=None)
    garage_id: int | None = Field(description='--> garage.id',
                                  default=None)
    parking_id: int | None = Field(description='--> parking_space.id',
                                   default=None)
    parcels_id: int | None = Field(description='--> parcels.id',
                                   default=None)
    rooms_id: int | None = Field(description='--> rooms.id',
                                 default=None)
    apart_id: int | None = Field(description='apartment.id',
                                 default=None)
    latitude: str = Field(description='Широта', default='00\'00000"')
    longitude: str = Field(description='Долгота', default='00\'00000"')


class RealEstateID(BaseModel):
    id: int = Field(description='ID недвиж')


class RealEstateView(BaseRealEstate, RealEstateID):
    pass


class RealEstateCreate(BaseRealEstate):
    pass


class RealEstateUpdate(BaseRealEstate, RealEstateID):
    pass

# #############################################################


class RealEstateResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: RealEstateView | None = None


class RealEstateError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class RealEstatePage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[RealEstateView] | None = None
    total: int
    page: int
    size: int
    pages: int


class RealEstatePageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class RealEstateDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    ads: Mappeds['Ads'] = relationship(back_populates='realest',
                                       uselist=False)
    contacts: Mappeds['Contacts'] = relationship(back_populates='realest',
                                                uselist=False)

    latitude  'Широта'
    longitude 'Долгота'
"""
