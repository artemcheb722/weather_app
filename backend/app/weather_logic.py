from fastapi import APIRouter, HTTPException
from pyowm import OWM

from .settings import settings

weather_router = APIRouter()

_owm = OWM(settings.API_KEY_WEATHER)
_manager = _owm.weather_manager()


@weather_router.get("/get_weather")
async def get_weather(city: str) -> dict:
    if not city:
        raise HTTPException(
            status_code=404,
            detail="City not found, Are you sure you wrote the name correctly?",
        )

    observation = _manager.weather_at_place(city)
    weather = observation.weather
    temp = weather.temperature("celsius")
    wind = weather.wind()

    return {
        "city": city,
        "temperature": temp["temp"],
        "feels_like": temp["feels_like"],
        "humidity": weather.humidity,
        "status": weather.detailed_status,
        "visibility": getattr(weather, "visibility_distance", None),
        "wind_speed": wind.get("speed", 0),
        "pressure": weather.pressure.get("press", 0),
    }
