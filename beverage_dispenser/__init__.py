from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import pymongo
from .routers import router
from .constants import env
from starlette.responses import JSONResponse
from .middlewares.initializer_middleware import InitializerMiddleware

# Enable/Disable Swagger Schema
docs_url = "/docs" if env.APP_DEBUG else None

app = FastAPI(
    title="Beverage Dispenser API",
    version="1.0.0",
    docs_url=docs_url,
    redoc_url=None
)

app.debug = env.APP_DEBUG

app.add_middleware(
    CORSMiddleware,
    allow_origins=env.ALLOWED_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index():
    return JSONResponse(
        content={"beverage-dispenser": {"status": "up"}},
        status_code=200,
        headers={"content-type": "application/json"},
    )

app.middleware("http")(InitializerMiddleware())

# APIs
app.include_router(router.router)
