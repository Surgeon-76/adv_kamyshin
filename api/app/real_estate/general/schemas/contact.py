from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class BaseContacts(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    realest_id: int = Field(description='--> real_estate.id')
    place_ads: str = Field(description='Размещает объявление',
                           default='Собственник')
    email: str | None = Field(description='Email',
                              nullable=True)
    phone: str = Field(description='Телефон',
                       nullable=False)
    communication: str = Field(description='Способ связи',
                               default='Звонки и сообщения')
    online: bool = Field(description='Онлайн показ',
                         default=False)


class ContactsID(BaseModel):
    id: int = Field(description='ID контакта')


class ContactsView(BaseContacts, ContactsID):
    pass


class ContactsCreate(BaseContacts):
    pass


class ContactsUpdate(BaseContacts, ContactsID):
    pass

# #############################################################


class ContactsResp(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: ContactsView | None = None


class ContactsError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: dict | None = None


class ContactsPage(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    status: str = 'succes'
    status_code: int = 200
    payload: list[ContactsView] | None = None
    total: int
    page: int
    size: int
    pages: int


class ContactsPageError(BaseModel):
    status: str = 'failure'
    status_code: int
    payload: list | None = None


class ContactsDel(BaseModel):
    status: str = 'succes'
    status_code: int
    payload: dict | None = None


"""
    place_ads 'Размещает объявление: Собственник, Посредник'
    email 'Email' 
    phone 'Телефон'
    communication'Способ связи: Звонки и сообщения, Только звонки,
                  Только сообщения'
    online 'Онлайн показ: Проведу, Не хочу'
"""
