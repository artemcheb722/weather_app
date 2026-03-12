from fastapi import FastAPI

from .settings import settings
from .weather_logic import weather_router


def get_application() -> FastAPI:
    app = FastAPI(root_path="/api", root_path_in_servers=True, debug=settings.DEBUG)

    app.include_router(weather_router, prefix="/weather", tags=["weather"])

    return app
