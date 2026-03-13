from fastapi import APIRouter
from .settings import settings
from pyowm import OWM
weather_router = APIRouter()

_owm = OWM(settings.API_KEY_WEATHER)
_manager = _owm.weather_manager()

@weather_router.post("/check")
async def get_weather():
    return {"city": "Kyiv", "temperature": 21, "status": "sunny"}


@weather_router.get("/get_weather")
async def get_weather(city: str) -> dict:
    observation = _manager.weather_at_place(city)
    weather = observation.weather

    return {
        "city": city,
        "temperature": weather.temperature("celsius")["temp"],
        "feels_like": weather.temperature("celsius")["feels_like"],
        "humidity": weather.humidity,
        "status": weather.detailed_status,
    }

