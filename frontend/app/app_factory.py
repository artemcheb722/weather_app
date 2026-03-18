from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers_for_rendering.routers import router
from settings import settings


def get_application() -> FastAPI:
    app = FastAPI(debug=settings)
    app.include_router(router)

    app.mount("/static", StaticFiles(directory="static"), name="static")
    return app
