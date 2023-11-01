from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BasePhoto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    ads_id: int = Field(description='--> ads.id')
    url: str = Field(description='url-путь изображения',
                     default='')


class PhotoID(BaseModel):
    id: int = Field(description='ID объявления')


class PhotoView(BasePhoto, PhotoID):
    pass


class PhotoCreate(BasePhoto):
    pass


class PhotoUpdate(BasePhoto, PhotoID):
    pass

# #############################################################


class PhotoResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: PhotoView | None = None


class PhotoError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class PhotoPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[PhotoView] | None = None
    total: int
    page: int
    size: int
    pages: int


class PhotoPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class PhotoDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    ads: Mapped['Ads'] = relationship(back_populates='photo')

    turl 'url-путь изображения'
"""
