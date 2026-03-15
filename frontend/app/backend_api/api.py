import httpx

from .settings import settings


async def get_weather(city: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{settings.BACKEND_START}/weather/get_weather", params={"city": city}
        )
    return response.json()
