from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseCategory(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    parent_id: int = Field(description='--> category.id')
    title: str = Field(description='Наименование категории')



class CategoryID(BaseModel):
    id: int = Field(description='ID категории')


class CategoryView(BaseCategory, CategoryID):
    pass


class CategoryCreate(BaseCategory):
    pass


class CategoryUpdate(BaseCategory, CategoryID):
    pass

# #############################################################


class CategoryResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: CategoryView | None = None


class CategoryError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class CategoryPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[CategoryView] | None = None
    total: int
    page: int
    size: int
    pages: int


class CategoryPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class CategoryDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    children: Mapped['Category'
                     ] = relationship(back_populates='parent',
                                      cascade="all, delete-orphan",)
    parent: Mapped['Category' | None
                   ] = relationship(back_populates='children',
                                    remote_side=[id])

    ads: Mapped[list['Ads']] = relationship(back_populates='category')

    title     'Наименование категории'
"""
