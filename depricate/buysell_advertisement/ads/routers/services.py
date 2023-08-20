from fastapi import (
                    APIRouter,
                    HTTPException,
                    status
                    )

from ..models.services import Service


app = APIRouter(
    prefix='/services',
    tags=['Услуги:']
)


@app.get("/", summary=('Список Услуг'))
async def get_list():
    return await Service.objects.limit(30).all()


@app.get('/{id}/', summary=('Услуга по id'))
async def get_one(id: int):
    service = await Service.objects.get_or_none(id=id)
    if not service:
        raise HTTPException(status_code=404, detail="Item not found")
    return service


@app.post('/create/', summary=('Добавить новую услугу'),
          status_code=status.HTTP_201_CREATED)
async def create(new_service: Service):
    await new_service.save()
    return new_service


@app.delete('/delete/{id}', summary='Удаление Услуги'
            )
async def delete(id: int):
    service = await Service.objects.get(id=id)
    return await service.delete()
