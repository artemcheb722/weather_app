from fastapi import FastAPI
from .app_factory import get_application

app = get_application()


@app.get("/")
async def index():
    return {"status2332": 200}


@app.get("/weather")
async def get_weather():
    return {
        "city": "Kyiv",
        "temperature": 21,
        "status": "sunny"
    }


app.root_path = "/api"

