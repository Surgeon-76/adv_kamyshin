from fastapi import (
    FastAPI,
    Request
)
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.staticfiles import StaticFiles

from settings.db import (
    database,
    metadata,
    engine
)

from buysell_advertisement.categories.routers import categories as categories
from buysell_advertisement.ads.routers import ads as ads
from buysell_advertisement.ads.routers import services as services
from users.routers import users as users
from users.routers import auth as auth
from buysell_advertisement.ads.routers import image_ads as image_gallery
from email_message.router import app as email_router
from tools import generate_content as generate

from apartments.main import app as appart
from buysell_advertisement.main import app as appads


app = FastAPI(
    # root_path="/api/v1",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
    title="https://kamyshin.ru",
    description="Камышинский портал по поиску услуг, недвижимости, авто и прочей ЛАБУДЫ)))",
    servers=[
        {'url': 'http://localhost:8000'},
        {"url": "http://localhost:8000/api/v1/advertisement/docs",
            "description": "Доска объявлений и услуг"},
        {"url": "http://localhost:8000/api/v1/apartments/docs",
            "description": "Жильё"},
    ],
)


app.mount("/api/v1/static", StaticFiles(directory="static"), name="static")
app.mount('/api/v1/apartments', appart)
app.mount('/api/v1/advertisement', appads)


app.state.database = database
metadata.create_all(engine)


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


origins = [
    "http://localhost:8000",
    "http://localhost:8080",
    'http://front:8080',
    'http://localhost:3000',
    'http://localhost:8080',
    'http://194.58.88.9:8080/'
    'http://194.58.88.9:3000/'
    'http://194.58.88.9:3001/'
    'http://front:3001',
    'http://front:3000',
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users.app)
app.include_router(auth.app)
app.include_router(generate.app)
app.include_router(email_router)
