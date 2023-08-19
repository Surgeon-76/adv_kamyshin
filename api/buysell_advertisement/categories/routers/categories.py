from typing import (
    Optional,
    List
)

from fastapi import (
                    APIRouter,
                    HTTPException,
                    status
                    )

from ..models.categories import Category
from ..schemas.category import (
    CreateUpdateCategory,
    GetCategories
)


app = APIRouter(
                prefix='/categories',
                tags=['Категории:']
                )


@app.get("/search/", summary=('Автопоиск Категорий'))
async def get_list(search: str, category_parent: Optional[int] = None):
    if category_parent:
        categories = await Category.objects.limit(10).select_related(
            ['parent_category__parent_category',
                "parent_category__parent_category__parent_category"]
            ).filter(name__icontains=search,
                     parent_category__id=category_parent
                     ).all()
    else:
        categories = await Category.objects.limit(10).select_related(
            ['parent_category__parent_category',
                "parent_category__parent_category__parent_category"]
            ).filter(name__icontains=search,
                     parent_category__isnull=False).all()
    response = [GetCategories.from_orm(category) for category in categories]
    return response


@app.get("/parents/", summary=('Список категорий'),
         response_model=List[GetCategories])
async def get_list_parent(limit: int, id: Optional[int] = None):
    if id:
        return await Category.objects.prefetch_related(
            ['parent_category__parent_category',
                "parent_category__parent_category__parent_category"]
        ).filter(parent_category=id).limit(limit).all()

    return await Category.objects.filter(parent_category=None
                                         ).limit(limit).all()


@app.get("/popular/", summary=('Список популярных категорий'))
async def get_list_popular(limit: int):
    return await Category.objects.filter(popular=True).limit(limit).all()


@app.get("/childs/", summary=('Список дочерних категорий'))
async def get_list_child(limit: int, slug: str):
    return await Category.objects.filter(
        parent_category__slug=slug).limit(limit).all()

# @app.get("/{slug}/", summary=('Категория по слагу'))
# async def get_list_child(slug:str):
#     return await Category.objects.get_or_none(slug = slug)


@app.get('/{id}/', summary=('Категория по id'), response_model=GetCategories)
async def get_one_category(id: int):
    category = await Category.objects.select_related(
        ['parent_category__parent_category',
            "parent_category__parent_category__parent_category"]
        ).get_or_none(id=id)
    if not category:
        raise HTTPException(status_code=404, detail="Item not found")

    return dict(category)


@app.get('/slug/{slug}/', summary=('Категория по slug'))
async def get_slug(slug: str):
    category = await Category.objects.get_or_none(slug=slug)
    if not category:
        raise HTTPException(status_code=404, detail="Item not found")
    return category


@app.post('/create/', summary=('Добавить новую категорию'),
          status_code=status.HTTP_201_CREATED)
async def create(new_category: CreateUpdateCategory):
    return await Category(**new_category.dict()).save()


@app.put('/update/{id}/', summary='Редактирование категории',
         status_code=status.HTTP_201_CREATED)
async def update(id: int, item: CreateUpdateCategory):
    category = await Category.objects.get_or_none(id=id)
    return await category.update(**item.dict())


@app.delete('/delete/{id}/', summary='Удаление категории',
            status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int):
    category = await Category.objects.get_or_none(id=id)
    if not category:
        raise HTTPException(status_code=404, detail="Item not found")
    return await category.delete()
