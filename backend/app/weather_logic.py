from fastapi import APIRouter, HTTPException
from pyowm import OWM

from .settings import settings

weather_router = APIRouter()

_owm = OWM(settings.API_KEY_WEATHER)
_manager = _owm.weather_manager()


@weather_router.get("/get_weather")
async def get_weather(city: str) -> dict:
    observation = _manager.weather_at_place(city)
    weather = observation.weather
    if not city:
        raise HTTPException(status_code=404, detail="City not found, Are you sure you wrote the name correctly?")
    else:
        return {
            "city": city,
            "temperature": weather.temperature("celsius")["temp"],
            "feels_like": weather.temperature("celsius")["feels_like"],
            "humidity": weather.humidity,
            "status": weather.detailed_status,
        }
