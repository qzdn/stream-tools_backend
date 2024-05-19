import requests
from datetime import datetime


def request_to_openweathermap(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)
    return response.json()


def get_weather_data(format, data):
    name = data["name"]
    weather_description = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    temp_feel = data["main"]["feels_like"]
    wind_degree = data["wind"]["deg"]
    wind_speed = data["wind"]["speed"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    match (format):
        case "txt":
            return f"{name} - сейчас {weather_description}. Температура {round(temp)}°C (по ощущению {round(temp_feel)}°C). Ветер - {wind_degrees_to_direction(wind_degree)}, {wind_speed} м/с. Влажность - {humidity}%, давление ~{pressure_to_mm(pressure)} мм рт. ст."
        case "json":
            return {
                "name": name,
                "weather_description": weather_description,
                "temp": temp,
                "temp_feel": temp_feel,
                "humidity": humidity,
                "pressure": pressure,
                "wind_speed": wind_speed,
                "wind_degree": wind_degree,
            }


def wind_degrees_to_direction(degrees):
    # https://en.wikipedia.org/wiki/Compass_rose
    directions = ["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
    index = int((degrees + 22.5) // 45 % 8)
    return directions[index]


# hPa to mm of mercury
def pressure_to_mm(pressure):
    return round(pressure / 1.333, 1)


def timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp)
