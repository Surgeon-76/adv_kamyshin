import random
import uuid

from sqlalchemy import (
    select,
    func
)
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import (
    APIRouter,
    status,
    Depends
)
from faker import Faker

from config.database import (
    Base,
    engine
)
from config.sessions import get_session
# from app.service.models.service import Service
# from app.service.models.company_wash_service import CompWashService
# from app.car.model import Auto
# from app.location.models.city import City
# from app.location.models.metroline import MetroLine
# from app.location.models.metrostation import MetroStation
# from app.auth.services.hash_pass import get_hashed_password
# from app.users.models.client import Client
# from app.users.models.manager import (
#     Manager,
#     Role
# )
# from app.company.model import WashingCompany
# from app.payment.model import (
#     Payment,
#     StatusPayment
# )
# from app.order.model import (
#     Order,
#     StatusOrder
# )


app = APIRouter(
    prefix="/api/v1/generate",
    tags=["Генератор контента:"]
)


fake = Faker(locale="ru_RU")


async def database_clear():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_auto(db: AsyncSession):

    for i in range(1, 31):
        new_car = {
            "car_brand": f"атобренд {i}",
            "car_model": f"модель авто {random.randint(1, 20)}"
            }
        car = Auto(**new_car)
        async with db.begin():
            db.add(car)
            await db.commit()

        print(f"Автомобиль: {car.car_brand} {car.car_model} создан")


async def create_city(db: AsyncSession):

    Faker.seed(0)
    for _ in range(1, 101):
        new_city = {
            "name": f"{fake.unique.city_name()}"
            }
        city = City(**new_city)
        async with db.begin():
            db.add(city)
            await db.commit()

        print(f"Город {city.name} создан")


async def create_metroline(db: AsyncSession):

    Faker.seed(0)

    city_id_list = [random.randint(1, 100) for _ in range(1, 71)]
    city_id_list = list(set(city_id_list))

    for i in range(1, len(city_id_list)):
        for _ in range(random.randint(1, 15)):
            new_metroline = {
                "name": f"Линия-'{fake.color_name()}'",
                "city_id": city_id_list[i]
                }
            metroline = MetroLine(**new_metroline)
            async with db.begin():
                db.add(metroline)
                await db.commit()
            print(f"{metroline.name}города с ID {metroline.city_id} создана")


async def create_metrostation(db: AsyncSession):

    count_metro = await db.scalar(select(func.count()).select_from(MetroLine))
    for i in range(1, count_metro + 1):
        metroline = await db.get(MetroLine, i)
        quantity = random.randint(1, 10)
        for j in range(1, quantity):
            new_metrostation = {
                "name": f"Станция {j} {metroline.name}-{i}",
                "metroline_id": i
                }
            metrostation = MetroStation(**new_metrostation)
            db.add(metrostation)
            await db.commit()
            print(f"{metrostation.name} создана")


async def create_client(db: AsyncSession):

    Faker.seed(0)
    password = get_hashed_password('123')
    for _ in range(1, 101):
        new_client = {
            "email": f"{fake.unique.email(safe=True, domain='yandex.ru') }",
            "telegram_username": f"@{fake.user_name()}",
            "phone": f"{fake.unique.phone_number()}",
            "password": password
            }
        client = Client(**new_client)
        db.add(client)
        await db.commit()
        print(f"Клиент {client.telegram_username} создан")


async def create_manager(db: AsyncSession):

    count_company = await db.scalar(select(
        func.count()).select_from(WashingCompany))
    Faker.seed(0)
    password = get_hashed_password('123')
    for _ in range(1, 101):
        new_manager = {
            "email": f"{fake.unique.email(safe=True, domain='yandex.ru') }",
            "password": password,
            "washing_company_id": random.randint(1, count_company),
            "role": Role.admin
            }
        manager = Manager(**new_manager)
        db.add(manager)
        await db.commit()
        print(f"Менеджер {manager.email} создан")
    super_admin = Manager(email="admin@mail.ru",
                          password=password,
                          washing_company_id=1,
                          role=Role.superadmin)
    db.add(super_admin)
    await db.commit()
    print(f"Супер Менеджер {super_admin.email} создан")


async def create_washing_company(db: AsyncSession):

    Faker.seed(0)
    count_metro = await db.scalar(select(
        func.count()).select_from(MetroStation))

    for _ in range(1, 51):
        num = random.randint(1, count_metro)
        row = await db.execute(
            select(MetroStation, MetroLine, City).
            where(MetroStation.id == num,
                  MetroLine.id == MetroStation.metroline_id,
                  City.id == MetroLine.city_id)
            )
        for i in row.scalars():
            res = i

        new_washing_company = {
            "name": f"{fake.unique.company()}",
            "address": f"{fake.unique.street_address()} ",
            "latitude": "15'6654''",
            "longitude": "56'887456''",
            "metro_station_id": res.id,
            "city_id": res.metroline.city_id,
            "logo": "logo.gif",
            "moderation": False,
            "phone": f"{fake.unique.phone_number()}"
            }
        washing_company = WashingCompany(**new_washing_company)
        db.add(washing_company)
        await db.commit()
        print(f"Компания: {washing_company.name} создана")


async def create_payment(db: AsyncSession):

    Faker.seed(0)

    for i in range(1, 51):
        new_payment = {
            "id_payment_acquiring": uuid.uuid4(),
            "summa": round(random.uniform(1000, 3000), 2),
            "status": StatusPayment.paid
            }
        if i % 2 == 0:
            new_payment.pop('status')
        payment = Payment(**new_payment)
        db.add(payment)
        await db.commit()
        print(f"Платёж с UUID: {payment.id_payment_acquiring} создан")


async def create_order(db: AsyncSession):

    Faker.seed(0)

    count_client = await db.scalar(select(
        func.count()).select_from(Client))
    count_company = await db.scalar(select(
        func.count()).select_from(WashingCompany))
    count_auto = await db.scalar(select(
        func.count()).select_from(Auto))
    count_payment = await db.scalar(select(
        func.count()).select_from(WashingCompany))

    for i in range(1, 101):
        new_order = {
            "client_id": random.randint(1, count_client),
            "washing_company_id": random.randint(1, count_company),
            "auto_id": random.randint(1, count_auto),
            "payment_id": random.randint(1, count_payment),
            "number_auto": f"{fake.plate_letter().lower()}{fake.unique.plate_number ()}{fake.plate_letter().lower()}{fake.plate_letter().lower()}",
            "status": StatusOrder.paid,
            "summa": round(random.uniform(1000, 5000), 2)
            }
        if i % 2 == 0:
            new_order.pop('status')
        order = Order(**new_order)
        db.add(order)
        await db.commit()
        print(f"Заказ мойки для авто Рег № {order.number_auto} создан")


async def create_services(db: AsyncSession):

    row = await db.execute(select(WashingCompany))

    for company in row.scalars().all():
        print(f"№: {company.id}, {company}")
        count_services = random.randint(1, 10)
        for num in range(1, count_services + 1):
            cws = CompWashService(price=round(random.uniform(300, 700), 2))
            new_service = {
                "name": f"Сервис {num} компании {company.name}",
                "logo": "logo.gif"
                }
            cws.service = Service(**new_service)
            cws.washing_company_id = company.id
            db.add(cws.service)
            await db.commit()
            print(f"{cws.service_name} создан")
        print('**************************************************************')
        print(f"{company} обновлёно")
        print('##############################################################')


@app.post("/debug/", summary=("Отладка"))
async def debug_function(db: AsyncSession = Depends(get_session)):
    return {"отладка закончена": "генератор рабочий!)))"}


@app.post("/", summary=("Генератор"))
async def generate_all(db: AsyncSession = Depends(get_session)):

    await create_auto(db)
    await create_city(db)
    await create_metroline(db)
    await create_metrostation(db)
    await create_client(db)
    await create_washing_company(db)
    await create_manager(db)
    await create_payment(db)
    await create_order(db)
    await create_services(db)

    return {"create": "ok"}


@app.delete('/clear/', summary=('Очистка базы данных'),
            status_code=status.HTTP_204_NO_CONTENT)
async def clear_db():
    # db: AsyncSession = Depends(get_session)
    #  user: str = Depends(get_current_user)
    await database_clear()
    return {"clear": "ok"}
