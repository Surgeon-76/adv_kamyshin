from fastapi import (
    APIRouter,
    UploadFile,
    HTTPException,
    status,
    File,
    Form
)

from ..models.photo import PhotoAPRT
from services.photo_image import (
    image_add,
    image_add_origin,
    image_delete
)


app = APIRouter(
    prefix='/advertisement/photo',
    tags=['Галерея фотографий недвижимости:']
)


@app.get('/list/', summary=('Все изображения'))
async def get_image(limit: int = 40):
    return await PhotoAPRT.objects.limit(limit).all()


@app.post('/', summary=('Добавить фото'),
          status_code=status.HTTP_201_CREATED)
async def add_image(advert_id: int = Form(...), image: UploadFile = File(...)):
    image_path_origin = await image_add_origin(image)
    image_path_thumb = await image_add(image)
    return await PhotoAPRT(
                advaprt=advert_id,
                photo=image_path_origin,
                photo_thumb=image_path_thumb
                ).save()


@app.put('/update/', summary=('Изменить фото'),
         status_code=status.HTTP_201_CREATED)
async def update_image(id: int = Form(...), new_image: UploadFile = File(...)):
    image = await PhotoAPRT.objects.get_or_none(id=id)
    if not image:
        raise HTTPException(status_code=404, detail="Item not found")
    await image_delete(image.photo, image.photo_thumb)
    image.photo = await image_add_origin(new_image)
    image.photo_thumb = await image_add(new_image)

    return await image.update()


@app.delete('/delete/', summary=('Удалить фото'),
            status_code=status.HTTP_204_NO_CONTENT)
async def delete_image(id: int):
    image = await PhotoAPRT.objects.get_or_none(id=id)
    if not image:
        raise HTTPException(status_code=404, detail="Item not found")
    await image_delete(image.photo, image.photo_thumb)

    return await image.delete()
