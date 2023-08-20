from typing import (
    Optional,
    Union
)
from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends
)
from services.auth import AuthJWT
from pydantic import parse_obj_as


from ..schemas.ads import CreateADs, UpdateADs, DateEnum, AdsGetOne
from services.api_responses import PaginationsResponses
from buysell_advertisement.categories.models.categories import Category
from buysell_advertisement.categories.routers.categories import (
    get_one_category
)
from ..models.ads import ADVT


app = APIRouter(
    prefix='/ads',
    tags=['Обьявления:']
)


@app.get("/", summary=('Список объявлений'))
async def get_list(
    page: int,
    page_size: int,
    category: Union[str, None] = None,
    date: Optional[DateEnum] = None
):
    order = '-id'
    if date:
        if date == DateEnum.new:
            order = '-id'
        else:
            order = 'id'

    if category:
        query = ()
        query = (
            ADVT.category.slug == category
        ) | (
            ADVT.category.parent_category.slug == category
        ) | (
            ADVT.category.parent_category.parent_category.slug ==
            category
        )

        total = await ADVT.objects.filter(query).count()

        results = await ADVT.objects.select_related(
            ['service',
                'category__parent_category__parent_category__parent_category']
        ).exclude_fields(
            ['user', 'photo_galery']
        ).order_by(order).paginate(page, page_size).filter(query).all()

    else:

        total = await ADVT.objects.count()

        results = await ADVT.objects.prefetch_related(
            ['service',
                'category__parent_category__parent_category']
        ).order_by(order).paginate(page, page_size).all()

    res = []

    for item in results:
        new_dict_category = parse_obj_as(AdsGetOne, item)
        itemn = item.dict()
        itemn['category'] = dict(new_dict_category.category)
        res.append(itemn)

    response: PaginationsResponses = PaginationsResponses(
        total,
        page,
        page_size,
        res
    )
    return response.get_responses


@app.get("/user/", summary=('Список объявлений по id user'))
async def get_list_user(
    Authorize: AuthJWT = Depends()
):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    # total = await ADVT.objects.filter(user__id=current_user).count()

    results = await ADVT.objects.select_related(
            ['service', 'user',
                'category__parent_category__parent_category__parent_category']
        ).exclude_fields(
            ['photo_galery']
        ).order_by('-id').filter(user=current_user).all()

    # res = []

    # for item in results:
    #     new_dict_category = parse_obj_as(AdsGetOne, item)
    #     itemn = item.dict()
    #     itemn['category'] = dict(new_dict_category.category)
    #     res.append(itemn)

    return results


@app.get('/{id}/', summary=('Объявление по id'))
async def get_one_count(id: int, count_views: Optional[int] = None):
    ad = await ADVT.objects.prefetch_related(
        ['service', 'photo_galery', 'category__parent_category']
    ).exclude_fields(
        ['user']
    ).get_or_none(id=id)
    if count_views:
        ad.count_views = count_views
        await ad.update()
    if not ad:
        raise HTTPException(status_code=404, detail="Item not found")

    itemn = ad.dict()
    itemn['category'] = await get_one_category(itemn['category']['id'])

    similar_ads = await ADVT.objects.prefetch_related(
        ['service', 'category',
         'category__parent_category__parent_category__parent_category']
    ).filter(category__id=itemn['category']['id']).limit(10).all()

    similar_list = []
    for item in similar_ads:
        itemn2 = item.dict()
        itemn2['category'] = await get_one_category(itemn['category']['id'])
        similar_list.append(itemn2)
    ad = AdsGetOne(**itemn)

    if ad.category.parent_category.parent_category:
        parent_category = ad.category.parent_category.id

    categories_list = []
    categories = await Category.objects.prefetch_related(
        ['parent_category__parent_category',
            "parent_category__parent_category__parent_category"]
    ).filter(parent_category=parent_category).limit(25).all()
    for item in categories:
        cat = await get_one_category(item.id)
        categories_list.append(cat)

    return {'ads': ad, 'categories': categories_list,
            'similar_ads': similar_list}


@app.get('/{id}/', summary=('Объявление по id'))
async def get_one(id: int):
    ad = await ADVT.objects.prefetch_related(
        ['service', 'photo_galery', 'category__parent_category']
    ).exclude_fields(
        ['user']
    ).get_or_none(id=id)
    if not ad:
        raise HTTPException(status_code=404, detail="Item not found")

    itemn = ad.dict()
    itemn['category'] = await get_one_category(itemn['category']['id'])

    similar_ads = await ADVT.objects.prefetch_related(
        ['service', 'category',
         'category__parent_category__parent_category__parent_category']
    ).filter(category__id=itemn['category']['id']).limit(10).all()

    similar_list = []
    for item in similar_ads:
        itemn2 = item.dict()
        itemn2['category'] = await get_one_category(itemn['category']['id'])
        similar_list.append(itemn2)
    ad = AdsGetOne(**itemn)

    if ad.category.parent_category.parent_category:
        parent_category = ad.category.parent_category.id

    categories_list = []
    categories = await Category.objects.prefetch_related(
        ['parent_category__parent_category',
            "parent_category__parent_category__parent_category"]
    ).filter(parent_category=parent_category).limit(25).all()
    for item in categories:
        cat = await get_one_category(item.id)
        categories_list.append(cat)

    return {'ads': ad, 'categories': categories_list,
            'similar_ads': similar_list}


@app.get('/slug/{slug}/', summary=('Объявление по slug'))
async def get_one_slug(slug: str):
    ad = await ADVT.objects.prefetch_related(
        ['service', 'photo_galery', 'category__parent_category']
    ).exclude_fields(
        ['user']
    ).get_or_none(slug=slug)
    if not ad:
        raise HTTPException(status_code=404, detail="Item not found")
    return ad


@app.post('/create/', summary=('Добавить новое объявление'),
          status_code=status.HTTP_201_CREATED)
async def create(new_ad: CreateADs):
    ad = ADVT(**new_ad.dict())
    # newads =  await ad.save_related(follow=True, save_all=True)
    return ad.save()


@app.put('/update/', summary=('Редактировать объявление'),
         status_code=status.HTTP_201_CREATED)
async def update(new_ad: UpdateADs):
    ad = ADVT(**new_ad.dict())
    await ad.save_related(follow=True, save_all=True)
    return ad


# @app.delete('/delete/{id}', summary='Удаление Обьявления'
#             )
# async def delete(id: int):
#     advt = await ADVT.objects.get(id=id)
#     await advt.service.clear(keep_reversed=False)
#     return await advt.delete()
