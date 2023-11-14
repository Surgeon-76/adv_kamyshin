from decimal import Decimal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseParcels(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    space: Decimal = Field(description='Площадь земельного участка',
                           max_digits=10,
                           decimal_places=2,
                           default=0.00)


class ParcelsID(BaseModel):
    id: int = Field(description='ID земельного участка')


class ParcelsView(BaseParcels, ParcelsID):
    pass


class ParcelsCreate(BaseParcels):
    pass


class ParcelsUpdate(BaseParcels, ParcelsID):
    pass

# #############################################################


class ParcelsResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: ParcelsView | None = None


class ParcelsError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class ParcelsPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[ParcelsView] | None = None
    total: int
    page: int
    size: int
    pages: int


class ParcelsPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class ParcelsDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    realest: Mapped['RealEstate'
                    ] = relationship(back_populates='parcels')

    space     'Площадь земельного участка'
"""
