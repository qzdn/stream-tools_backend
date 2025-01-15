import requests
from api.config import OWM_API_URL, OWM_API_KEY


def get_weather_data(city):
    params = {"q": city, "appid": OWM_API_KEY, "units": "metric", "lang": "ru"}
    response = requests.get(OWM_API_URL, params=params)

    if response.status_code != 200:
        return {"error": response.json()["message"]}

    data = response.json()
    try:
        result = {
            "name": data["name"],
            "weather_description": data["weather"][0]["description"],
            "temp": data["main"]["temp"],
            "temp_feel": data["main"]["feels_like"],
            "wind_deg": data["wind"]["deg"],
            "wind_direction": _wind_degrees_to_direction(data["wind"]["deg"]),
            "wind_speed": data["wind"]["speed"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "pressure_mm": _pressure_to_mm(data["main"]["pressure"]),
        }
    except KeyError:
        result = {"error": "Ошибка при парсинге данных"}

    return result


def _wind_degrees_to_direction(degrees):
    directions = ["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
    try:
        index = int((degrees + 22.5) // 45 % 8)
        return directions[index]
    except (TypeError, ValueError):
        return "неизвестно"


def _pressure_to_mm(pressure):
    try:
        return round(pressure / 1.333, 1)
    except (TypeError, ZeroDivisionError):
        return "неизвестно"
