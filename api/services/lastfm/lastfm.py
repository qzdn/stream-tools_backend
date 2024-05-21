import requests


def request_to_lastfm(username, api_key):
    url = f"http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={username}&api_key={api_key}&format=json&limit=1"
    response = requests.get(url)
    return response.json()


def get_tracks_data(format, data):
    artist = data["artist"]["#text"]
    track = data["name"]
    album = data["album"]["#text"]
    cover = data["image"][3]["#text"]

    if format == "txt":
        return f"{artist} - {track}"
    elif format == "json":
        return {
            "nowplaying": {
                "artist": artist,
                "track": track,
                "album": album,
                "cover": cover,
            }
        }
