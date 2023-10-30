from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseBrandMoto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    brand: str = Field(description='Бренд мото',
                       default='')
    logo: str = Field(description='Логотип',
                      default='')


class BrandMotoID(BaseModel):
    id: int = Field(description='ID бренда мото')


class BrandMotoView(BaseBrandMoto, BrandMotoID):
    pass


class BrandMotoCreate(BaseBrandMoto):
    pass


class BrandMotoUpdate(BaseBrandMoto, BrandMotoID):
    pass

# #############################################################


class BrandMotoResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: BrandMotoView | None = None


class BrandMotoError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class BrandMotoPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[BrandMotoView] | None = None
    total: int
    page: int
    size: int
    pages: int


class BrandMotoPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class BrandMotoDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    model: Mapped[list['ModelMoto']] = relationship(back_populates='brand')

    model 'Бренд мото'
    logo 'Логотип'
"""
