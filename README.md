# Twitch tools backend

Backend for variety Twitch tools like various APIs fetch, song requests and more. Prepared for deploying to [Vercel](https://vercel.com).

## How to run it locally?

```
python -m venv .venv
pipenv install
pipenv shell
mv ./.env.example ./.env
python ./main.py
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
