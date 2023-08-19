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
from .routers import category as category
from .routers import advertisement as advertisement
from .routers import address as address
from .routers import photo as images


app = FastAPI(
    title="Недвижимость",
    description="Жильё для ВСЕХ"
)
# app = FastAPI(openapi_url="/api/v1/movies/openapi.json", docs_url="/api/v1/movies/docs")
# app = FastAPI(openapi_url="/api/v1/casts/openapi.json", docs_url="/api/v1/casts/docs")


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


app.include_router(category.app)
app.include_router(advertisement.app)
app.include_router(address.app)
app.include_router(images.app)
