from fastapi import FastAPI
from .weather_logic import weather_router
from .settings import settings

def get_application() -> FastAPI:
    app = FastAPI(root_path="/api", root_path_in_servers=True, debug=settings.DEBUG)

    app.include_router(weather_router,prefix="/weather", tags=["weather"])

    return app