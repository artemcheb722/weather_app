from fastapi import APIRouter

weather_router = APIRouter()

@weather_router.post("/check")
async def get_weather():
    return {
        "city": "Kyiv",
        "temperature": 21,
        "status": "sunny"
    }