from backend_api.api import get_weather
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/get_weather")
async def get_weather_by_city(city: str, request: Request):
    get_weather_ex = await get_weather(city)

    return templates.TemplateResponse(
        "weather_page.html",
        {
            "request": request,
            "get_weather_ex": get_weather_ex,
        },
    )


@router.get("/")
async def main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@router.get("/weather_page")
async def weather_page(request: Request):
    return templates.TemplateResponse("weather_page.html", {"request": request})
