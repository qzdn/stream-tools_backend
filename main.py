from uvicorn import run

if __name__ == "__main__":
    run("api.index:app", host="0.0.0.0", port=3000)
