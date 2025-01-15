# Twitch tools backend

Backend for my personal Twitch tools like various APIs fetch, song requests and more. This project is designed to gain hands-on experience with Python, APIs, and backend development in general.

## How to run?

```sh
$ cp ./api/config_example.py ./api/config.py
$ python -m venv .venv
$ source ./.venv/bin/activate
$ pip install -r requirements.txt
$ python ./run.py
```

## Custom command in StreamElements

```
${customapi.https://PROJECT.vercel.app/lastfm?username=USERNAME}
${customapi.https://PROJECT.vercel.app/weather?city=$(1:)}
${customapi.https://PROJECT.vercel.app/hltb?gamename=$(1:)}
```
