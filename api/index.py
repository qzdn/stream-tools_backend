import os
from flask import Flask, request
from dotenv import load_dotenv

from api.services.hltb import request_to_hltb
from api.services.lastfm import get_tracks_data, request_to_lastfm
from api.services.openweathermap import get_weather_data, request_to_openweathermap


app = Flask(__name__)

load_dotenv()
LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")


@app.route("/", methods=["GET"])
def root():
    return {
        "methods": {
            "lastfm": "/lastfm/<string:username>?format=<string:format>",
            "weather": "/weather/<string:city>?format=<string:format>",
            "hltb": "/hltb/<string:game>?year=<string:year>&format=<string:format>",
        }
    }


@app.route("/song-requests", methods=["GET", "POST"])
def song_requests():
    return {
        "message": "TBD",
    }


@app.route("/lastfm/<string:username>", methods=["GET"])
def get_nowplaying_lastfm_track(username):
    format = request.args.get("format") or "txt"
    data = request_to_lastfm(username, LASTFM_API_KEY)

    if not data:
        match (format):
            case "txt":
                return "Ошибка получения данных"
            case "json":
                return {"message": "Ошибка получения данных"}

    if "error" in data:
        match (format):
            case "txt":
                return data["message"]
            case "json":
                return {"message": data["message"]}

    if "@attr" not in data["recenttracks"]["track"][0]:
        match (format):
            case "txt":
                return "Сейчас ничего не скробблится"
            case "json":
                return {"nowplaying": None}

    match (format):
        case "txt" | "json":
            return get_tracks_data(format, data["recenttracks"]["track"][0])
        case _:
            return "Некорректные параметры запроса"


@app.route("/weather/<string:city>", methods=["GET"])
def get_current_weather(city):
    format = request.args.get("format") or "txt"
    request_result = request_to_openweathermap(city, OPENWEATHERMAP_API_KEY)

    if request_result["cod"] != 200:
        match (format):
            case "txt":
                return request_result["message"]
            case "json":
                return {"message": request_result["message"]}

    if "weather" in request_result and "main" in request_result:
        match (format):
            case "txt" | "json":
                return get_weather_data(format, request_result)
            case _:
                return "Некорректные параметры запроса"


@app.route("/hltb/<string:game>", methods=["GET"])
def get_hltb_game(game):
    year = request.args.get("year") or None
    format = request.args.get("format") or "txt"

    if "*" in game and not game.startswith("*"):
        parts = game.split("*")
        game = parts[0]
        year = parts[1]

    match (format):
        case "txt" | "json":
            return request_to_hltb(game, year, format)
        case _:
            return "Некорректные параметры запроса"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
