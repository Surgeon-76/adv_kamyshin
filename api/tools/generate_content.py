import random
from fastapi import (
    APIRouter,
    status
)

from users.models.users import User
from buysell_advertisement.categories.models.categories import Category
from buysell_advertisement.ads.models.ads import ADVT
from buysell_advertisement.ads.models.image_ads import PhotoADVT
from apartments.models.categorie import (
    Categorie,
    TransactionVar,
    TypeOfHousing
)

from settings.db import (
    metadata,
    engine
)

from services.slug import generate_slug


app = APIRouter(
    prefix='/api/v1/generate',
    tags=['Генератор контента:']
)


async def database_clear():
    metadata.drop_all(bind=engine)
    metadata.create_all(bind=engine)


text = 'Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной "рыбой" для текстов на латинице с начала XVI века. В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов, используя Lorem Ipsum для распечатки образцов. Lorem Ipsum не только успешно пережил без заметных изменений пять веков, но и перешагнул в электронный дизайн. Его популяризации в новое время послужили публикация листов Letraset с образцами Lorem Ipsum в 60-х годах и, в более недавнее время, программы электронной вёрстки типа Aldus PageMaker, в шаблонах которых используется Lorem Ipsum.'
users = []


async def create_user():

    # user
    phone = 1111111111
    for user in range(10, 300):
        phone += 1
        new_user = {
            "email": f"string{user}",
            "phone": f'+7{phone}',
            "password": "string"
        }
        usern = await User(**new_user).save()
        users.append(usern)
        print(f'user {user}')

categories = []


async def create_category():
    parent_category_list = []
    for item in range(1, 30):

        parent_category = None

        data = {
            "name": f'Категория{item}',
            "parent_category": parent_category,
            "slug": generate_slug(f'Категория{item}'),
            "logo": '/static/images/images.jpeg',
            'popular': True
        }

        cat = await Category(**data).save()
        parent_category_list.append(cat)

    child_category_list = []
    for item in range(1, 400):
        parent_category = random.choice(parent_category_list)

        data = {
            "name": f'Категория-2 {item}',
            "parent_category": parent_category,
            "slug": generate_slug(f'Категория-2 {item}'),
            "logo": ''
        }

        cat = await Category(**data).save()
        child_category_list.append(cat)

    for item in range(1, 2000):
        parent_category = random.choice(child_category_list)

        data = {
            "name": f'Категория-3 {item}',
            "parent_category": parent_category,
            "slug": generate_slug(f'Категория-3 {item}'),
            "logo": ''
        }

        cat = await Category(**data).save()

        categories.append(cat)

list_ads = []


async def create_ads():
    phone = 1111111111
    itemc = 1
    for item in range(1, 2000):
        phone += 1
        itemc += item
        data = {
            "logo": '/static/images/images.jpeg',
            "agreement": True,
            "user": random.choice(users),
            "phone": f'+7{phone}',
            "title": f'Обьявление {item}',
            "descriptions": text,
            "category": random.choice(categories),

            "service": [
                {
                    "name": f'Услуга {itemc+1}',
                    "price": 112,
                    "unit_of_dim": random.choice([
                        'за услугу',
                        'за м*2',
                        'за м. погонный',
                        'за м*3',
                        'за 1 шт.',
                        'за 1 метр',
                        'за 1 км.',
                        'за 45 мин.',
                        'за 1 час',
                        'за 1 сутки',
                        'за 1 неделю',
                        'за 1 месяц',
                    ]),
                    "slug": generate_slug(f'Услуга {itemc+1}')
                },
                {
                    "name": f'Услуга {itemc+2}',
                    "price": 112,
                    "unit_of_dim": random.choice([
                        'за услугу',
                        'за м*2',
                        'за м. погонный',
                        'за м*3',
                        'за 1 шт.',
                        'за 1 метр',
                        'за 1 км.',
                        'за 45 мин.',
                        'за 1 час',
                        'за 1 сутки',
                        'за 1 неделю',
                        'за 1 месяц',
                    ]),
                    "slug": generate_slug(f'Услуга {itemc+2}')
                },
                {
                    "name": f'Услуга {itemc+3}',
                    "price": 112,
                    "unit_of_dim": random.choice([
                        'за услугу',
                        'за м*2',
                        'за м. погонный',
                        'за м*3',
                        'за 1 шт.',
                        'за 1 метр',
                        'за 1 км.',
                        'за 45 мин.',
                        'за 1 час',
                        'за 1 сутки',
                        'за 1 неделю',
                        'за 1 месяц',
                    ]),
                    "slug": generate_slug(f'Услуга {itemc+3}')
                },
                {
                    "name": f'Услуга {itemc+4}',
                    "price": 112,
                    "unit_of_dim": random.choice([
                        'за услугу',
                        'за м*2',
                        'за м. погонный',
                        'за м*3',
                        'за 1 шт.',
                        'за 1 метр',
                        'за 1 км.',
                        'за 45 мин.',
                        'за 1 час',
                        'за 1 сутки',
                        'за 1 неделю',
                        'за 1 месяц',
                    ]),
                    "slug": generate_slug(f'Услуга {itemc+4}')
                }
            ]
        }

        ad = ADVT(**data)
        await ad.save_related(follow=True, save_all=True)
        await ad.update(slug=generate_slug(str(ad.title)+str(ad.id)))
        list_ads.append(ad)
        if item % 2 == 0:
            for _ in range(0, 10):
                data = {
                    'photo': '/static/images/images.jpeg',
                    'photo_thumb': '/static/images/images.jpeg',
                    'adv': ad
                }
                await PhotoADVT(**data).save()

        print(itemc, generate_slug(f'Услуга {itemc+4}'))


async def create_appart_categorie():
    for num in range(1, 51):
        data = {
            "transaction": random.choice(
                [tranz.value for tranz in TransactionVar]),
            "type_housing": random.choice([typ.value for typ in TypeOfHousing]),
            "daily": random.randint(0, 1)
        }

        if data['transaction'] == TransactionVar.tv_1.value:
            data['daily'] = 0

        await Categorie(**data).save()
        print(f'Катгория {num} ({data["transaction"]}, {data["type_housing"]}) создана!')


@app.post("/", summary=('Генератор'))
async def generate_all():
    await create_user()
    await create_category()
    await create_ads()

    return {'create': 'ok'}


@app.post("/debug/", summary=("Отладка"))
async def debug_function():
    await create_appart_categorie()
    # create_rel_provider(db)
    # create_tender_trade(db)
    return {"отладка закончена": "генератор рабочий!)))"}


@app.delete('/clear/', summary=('Очистка базы данных'),
            status_code=status.HTTP_204_NO_CONTENT)
async def clear_db():
    await database_clear()

    return {"clear": "ok"}
