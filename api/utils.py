from flask import jsonify, Response


def format_data(data, format_type):
    if format_type == "json":
        return jsonify(data)
    elif format_type == "txt":
        txt_info = _format_as_txt(data)
        return Response(txt_info, mimetype="text/plain")


def _format_as_txt(data):
    # Last.fm
    if "artist" in data:
        return f"{data['artist']} - {data['track']}"

    # OpenWeatherMap
    elif "name" in data:
        return (
            f"{data['name']} - сейчас {data['weather_description']}. Температура {round(data['temp'])}°C "
            f"(по ощущению {round(data['temp_feel'])}°C). Ветер - {data['wind_direction']}, {data['wind_speed']} м/с. "
            f"Влажность - {data['humidity']}%, давление ~{data['pressure_mm']} мм рт. ст."
        )

    # HLTB
    elif "game_name" in data:
        return (
            f"{data['game_name']} ({data['release_world']}) :: "
            f"Main story - {data['main_story']} ч., Main+Extras - {data['main_extra']} ч., Completionist - {data['completionist']} ч. :: "
            f"{data['url']}"
        )

    return "Неизвестный формат данных"
