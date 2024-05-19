# Twitch tools backend

Backend for my personal Twitch tools like various APIs fetch, song requests and more. This project is designed to gain hands-on experience with Python, APIs, and backend development in general. Prepared for deploying to [Vercel](https://vercel.com).

## How to run it locally?

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mv ./.env.example ./.env
python ./run.py
```

```
${customapi.https://PROJECT.vercel.app/lastfm/USERNAME_HERE}
${customapi.https://PROJECT.vercel.app/weather/${1:}}
${customapi.https://PROJECT.vercel.app/hltb/${1:}}
```

## TODO:

- [x] Last.fm - "Scrobbling now" info
- [x] OpenWeatherMap - Current weather
- [x] HLTB - Game length info
- [ ] Steam - Prices, user info...

etc.:

- [ ] Docker image
- [ ] Stuff for song requests
- [ ] TBD
