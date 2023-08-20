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

from .categories.routers import categories as categories
from .ads.routers import ads as ads
from .ads.routers import services as services
from users.routers import users as users
from users.routers import auth as auth
from .ads.routers import image_ads as image_gallery


app = FastAPI(
    # root_path="/api/v1",
    # openapi_url="/api/v1/openapi.json",
    # docs_url="/api/v1/docs",
    title="Доска объявлений",
    description="Поиск услуг"
)


app.mount("/api/v1/static", StaticFiles(directory="static"), name="static")

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


app.include_router(categories.app)
app.include_router(ads.app)
app.include_router(services.app)
app.include_router(image_gallery.app)
