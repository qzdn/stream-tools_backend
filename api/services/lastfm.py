import requests
from api.config import LASTFM_API_URL, LASTFM_API_KEY


def get_lastfm_data(username):
    params = {
        "method": "user.getrecenttracks",
        "username": username,
        "api_key": LASTFM_API_KEY,
        "format": "json",
        "limit": 1,
    }
    response = requests.get(LASTFM_API_URL, params=params)
    if response.status_code != 200:
        return {"error": response.json()["message"]}

    data = response.json()
    try:
        info = data["recenttracks"]["track"][0]
        result = {
            "artist": info["artist"]["#text"],
            "track": info["name"],
            "album": info["album"]["#text"],
            "cover": info["image"][3]["#text"],
        }
    except KeyError:
        result = {"error": "Ошибка при парсинге данных"}

    return result
