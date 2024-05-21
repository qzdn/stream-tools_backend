import os
from fastapi import FastAPI, Response
from fastapi.websockets import WebSocket
from dotenv import load_dotenv

from api.mongodb.connection import select_from_mongo
from api.mongodb.models.RequestModel import User
from api.services.lastfm.lastfm import request_to_lastfm, get_tracks_data
from api.services.openweathermap.openweathermap import (
    request_to_openweathermap,
    get_weather_data,
)
from api.services.hltb.hltb import request_to_hltb

app = FastAPI()

load_dotenv()
LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")


@app.get("/")
async def root():
    return {"message": "See /docs for info"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


@app.get("/song-requests/", response_model=User, status_code=200)
async def get_song_requests(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return select_from_mongo()


@app.get("/lastfm/{username}")
async def get_nowplaying_lastfm_track(username, format: str = "txt"):
    data = request_to_lastfm(username, LASTFM_API_KEY)

    if not data:
        if format == "txt":
            return "Ошибка получения данных"
        elif format == "json":
            return {"message": "Ошибка получения данных"}

    if "error" in data:
        if format == "txt":
            return data["message"]
        elif format == "json":
            return {"message": data["message"]}

    if "@attr" not in data["recenttracks"]["track"][0]:
        if format == "txt":
            return "Сейчас ничего не скробблится"
        elif format == "json":
            return {"nowplaying": None}

    if format == "txt" or "json":
        return get_tracks_data(format, data["recenttracks"]["track"][0])
    else:
        return "Некорректные параметры запроса"


@app.get("/weather/{city}")
async def get_current_weather(city, format: str = "txt"):
    request_result = request_to_openweathermap(city, OPENWEATHERMAP_API_KEY)

    if request_result["cod"] != 200:
        if format == "txt":
            return request_result["message"]
        elif format == "json":
            return {"message": request_result["message"]}

    if "weather" in request_result and "main" in request_result:
        if format == "txt" or "json":
            return get_weather_data(format, request_result)
        else:
            return "Некорректные параметры запроса"


@app.get("/hltb/{game}")
async def get_hltb_game(game, year: int = None, format: str = "txt"):
    if format == "txt" or "json":
        return request_to_hltb(game, year, format)
    else:
        return "Некорректные параметры запроса"
