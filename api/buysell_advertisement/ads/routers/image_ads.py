from fastapi import (
    File,
    UploadFile,
    APIRouter,
    Form
)
# from fastapi.responses import FileResponse
from ..models.image_ads import PhotoADVT
from services.photo_image import (
    image_add_origin,
    image_add
)


app = APIRouter(
    prefix='/ads/gallery',
    tags=['Галерея изображений объявлений:']
)


@app.post('/', summary=('Добавить изображение'))
async def add_image(ads_id: int = Form(...), image: UploadFile = File(...)):
    image_path_origin = await image_add_origin(image)
    image_path_thumb = await image_add(image)
    photo = await PhotoADVT(
                adv=ads_id,
                photo=image_path_origin,
                photo_thumb=image_path_thumb
                ).save()
    return photo


@app.get('/list/', summary=('Все изображение'))
async def get_image():
    photo = await PhotoADVT.objects.limit(40).all()
    return photo
