from fastapi import (
    APIRouter,
    HTTPException,
    status,
)

from ..models.categorie import Categorie
from ..schemas.categorie import (
    CategorieCreate,
    CategorieUpdate
)


app = APIRouter(
    prefix='/category',
    tags=['Категория:']
)


@app.get('/all/', summary=('Список категорий'),
         status_code=status.HTTP_200_OK)
async def search_all():
    return await Categorie.objects.all()


@app.post('/create/', summary=('Добавить новую категорию'),
          status_code=status.HTTP_201_CREATED)
async def create(new_category: CategorieCreate):
    print(new_category.dict())
    return await Categorie(**new_category.dict()).save()


@app.put('/update/{id}/', summary='Редактирование категории',
         status_code=status.HTTP_201_CREATED)
async def update(id: int, item: CategorieUpdate):
    category = await Categorie.objects.get_or_none(id=id)
    if not category:
        raise HTTPException(status_code=404, detail="Item not found")
    return await category.update(**item.dict())


@app.delete('/delete/{id}/', summary='Удаление категории',
            status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int):
    category = await Categorie.objects.get_or_none(id=id)
    if not category:
        raise HTTPException(status_code=404, detail="Item not found")
    return await category.delete()
