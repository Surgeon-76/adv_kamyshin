from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseBrandAuto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    brand: str = Field(description='Бренд авто',
                       default='')
    logo: str = Field(description='Логотип',
                      default='')


class BrandAutoID(BaseModel):
    id: int = Field(description='ID авто бренда')


class BrandAutoView(BaseBrandAuto, BrandAutoID):
    pass


class BrandAutoCreate(BaseBrandAuto):
    pass


class BrandAutoUpdate(BaseBrandAuto, BrandAutoID):
    pass

# #############################################################


class BrandAutoResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: BrandAutoView | None = None


class BrandAutoError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class BrandAutoPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[BrandAutoView] | None = None
    total: int
    page: int
    size: int
    pages: int


class BrandAutoPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class BrandAutoDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
model: Mapped[list['ModelAuto']] = relationship(back_populates='brand')

    model 'Бренд авто'
    logo 'Логотип'
"""
