import uvicorn


def start(app):
    uvicorn.run(app, host="127.0.0.1", port=8000)