from typing import Optional

from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends
)

from users.models.users import User

from ..models.categorie import (
    TransactionVar,
    TypeOfHousing,
    Categorie
)
from ..models.advertisement import (
    ADSAppart,
    AuxiliaryPremises,
    Finishing,
    NumberOfRooms,
    Recency,
    SanNode,
    TypeHouse
)
from ..models.photo import PhotoAPRT
from ..models.address import Address
from ..schemas.advertisement import (
    ADSAppartCreate,
    ADSAppartUpdate
)
from buysell_advertisement.ads.schemas.ads \
    import DateEnum
from services.api_responses import PaginationsResponses
from services.auth import AuthJWT

app = APIRouter(
    prefix='/advertisement',
    tags=['Недвижимость(объявления):']
)


@app.get('/all/', summary=('Все объявления'),
         status_code=status.HTTP_200_OK)
async def view_all():
    ad = await ADSAppart.objects.select_related(
        ['user',
         'category',
         'address',
         'photoaprts__advaprt']).all()
    return ad


@app.get('/filter/', summary=('Все объявления с пагинацией либо по фильтру'),
         status_code=status.HTTP_200_OK)
async def view_all_page(
    page: int,
    page_size: int,
    date: DateEnum = 'new',
    numofroom: NumberOfRooms = None,
    recency: Recency = None,
    finishing: Finishing = None,
    auxiliary: AuxiliaryPremises = None,
    sannode: SanNode = None,
    typehouse: TypeHouse = None,
    closed: Optional[bool] = None,
    transactions: TransactionVar = None,
    typeofhousing: TypeOfHousing = None
):
    order = '-id'
    if date == DateEnum.bye:
        order = 'id'
    query = {}
    if numofroom:
        query['rooms'] = numofroom.value
    if recency:
        query['originality'] = recency.value
    if finishing:
        query['finish'] = finishing.value
    if auxiliary:
        query['auxiliary'] = auxiliary.value
    if sannode:
        query['sanitary'] = sannode.value
    if typehouse:
        query['buildingtype'] = typehouse.value
    if closed:
        query['closed'] = closed
    if transactions:
        query['category__transaction'] = transactions.value
    if typeofhousing:
        query['category__type_housing'] = typeofhousing.value

    total = await ADSAppart.objects.count()
    if total < 1:
        raise HTTPException(status_code=404, detail="Item not found")

    if len(query):
        res = await ADSAppart.objects.prefetch_related(
                ['user',
                 'category',
                 'address',
                 'photoaprts__advaprt']
            ).order_by(order).paginate(page, page_size).filter(**query).all()
        if not res:
            raise HTTPException(status_code=404, detail="Item not found")
    else:
        res = await ADSAppart.objects.prefetch_related(
                ['user',
                 'category',
                 'address',
                 'photoaprts__advaprt']
            ).order_by(order).paginate(page, page_size).all()

    response: PaginationsResponses = PaginationsResponses(
        total,
        page,
        page_size,
        res
    )
    return response.get_responses


@app.get('/{id}/', summary=('Объявление по id'),
         status_code=status.HTTP_200_OK)
async def view_one(id: int):
    ad = await ADSAppart.objects.select_related(
        ['user',
         'category',
         'address',
         'photoaprts__advaprt']).get_or_none(id=id)
    if not ad:
        raise HTTPException(status_code=404, detail="Item not found")
    return ad


@app.post('/create/', summary=('Добавить новое объявление'),
          status_code=status.HTTP_201_CREATED,
          )
async def create(new_ad: ADSAppartCreate,
                 Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    new_ad.user = Authorize.get_jwt_subject()
    return await ADSAppart(**new_ad.dict()).save()


@app.put('/update/', summary=('Редактировать объявление'),
         status_code=status.HTTP_201_CREATED)
async def update(new_ad: ADSAppartUpdate):
    ad = ADSAppart(**new_ad.dict())
    await ad.save_related(follow=True, save_all=True)
    return ad


@app.delete('/delete/{id}/', summary=('Удаление Обьявления'),
            status_code=status.HTTP_204_NO_CONTENT
            )
async def delete(id: int):
    current_user = id
    ad = await ADSAppart.objects.select_related(
        ['user',
         'category',
         'address',
         'photoaprts__advaprt']).get_or_none(id=id)
    if not ad:
        raise HTTPException(status_code=404, detail="Not found!")    
    if ad.user.admission == 2:
        if not current_user == ad.user.id:
            raise HTTPException(status_code=401, detail="No access!")
    deluser = await User.objects.get_or_none(id=ad.user.id)
    delcategory = await Categorie.objects.get_or_none(id=ad.category.id)
    deladdress = await Address.objects.get_or_none(id=ad.address.id)
    await PhotoAPRT.objects.filter(advaprt=ad.id).delete()
    await deluser.adsapparts.clear()
    await delcategory.adsapparts.clear()
    await deladdress.adsapparts.clear(keep_reversed=False)
    await Address.objects.delete(id=ad.address.id)

    return None





# async def delete(id: int, Authorize: AuthJWT = Depends()):
#     Authorize.jwt_required()
#     current_user = Authorize.get_jwt_subject()
#     ad = await ADSAppart.objects.select_related(
#         ['user',
#          'category',
#          'address',
#          'photoaprts__advaprt']).get_or_none(id=id)
#     if not ad:
#         raise HTTPException(status_code=404, detail="Not found!")    
#     if ad.user.admission == 2:
#         if not current_user == ad.user.id:
#             raise HTTPException(status_code=401, detail="No access!")

#     await PhotoAPRT.objects.filter(advapart=ad.id).delete()
#     await ad.user.clear()
#     #await Address.objects.delete(id=ad.address)

#     # ad = await ADSAppart.objects.get(id=id)
#     # if not ad:
#     #     raise HTTPException(status_code=404, detail="Item not found")
#     # return await ad.delete()
#     return 5
