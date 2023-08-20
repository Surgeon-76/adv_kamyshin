from fastapi import (
    APIRouter,
    HTTPException,
    status,
)

from ..models.address import Address
from ..schemas.address import (
    AddressCreate,
    AddressUpdate
)


app = APIRouter(
    prefix='/address',
    tags=['Адрес:']
)


@app.get('/all/', summary=('Список всех адресов'),
         status_code=status.HTTP_200_OK)
async def search_all():
    return await Address.objects.all()


@app.post('/create/', summary=('Добавить новый адрес'),
          status_code=status.HTTP_201_CREATED)
async def create(new_address: AddressCreate):
    return await Address(**new_address.dict()).save()


@app.put('/update/{id}/', summary='Изменить адрес',
         status_code=status.HTTP_201_CREATED)
async def update(id: int, item: AddressUpdate):
    address = await Address.objects.get_or_none(id=id)
    if not address:
        raise HTTPException(status_code=404, detail="Item not found")
    return await address.update(**item.dict())


@app.delete('/delete/{id}/', summary='Удалить адрес',
            status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int):
    address = await Address.objects.get_or_none(id=id)
    if not address:
        raise HTTPException(status_code=404, detail="Item not found")
    return await address.delete()
