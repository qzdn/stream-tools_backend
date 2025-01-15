from flask import Flask, jsonify, request
from api.utils import format_data
from api.services.lastfm import get_lastfm_data
from api.services.openweathermap import get_weather_data
from api.services.hltb import get_hltb_data

app = Flask(__name__)


def get_response_format():
    valid_formats = ["json", "txt"]
    format_type = request.args.get("format")
    if format_type not in valid_formats:
        return "txt"
    return format_type


@app.route("/lastfm", methods=["GET"])
def lastfm():
    user = request.args.get("username")
    if not user:
        return jsonify({"error": 'Параметр "username" обязателен'}), 400

    data = get_lastfm_data(user)
    format_type = get_response_format()

    return format_data(data, format_type)


@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": 'Параметр "city" обязателен'}), 400

    data = get_weather_data(city)
    format_type = get_response_format()

    return format_data(data, format_type)


@app.route("/hltb", methods=["GET"])
def hltb():
    gamename = request.args.get("gamename")
    if not gamename:
        return jsonify({"error": 'Параметр "gamename" обязателен'}), 400

    data = get_hltb_data(gamename)
    format_type = get_response_format()

    return format_data(data, format_type)


if __name__ == "__main__":
    app.run(debug=True)
