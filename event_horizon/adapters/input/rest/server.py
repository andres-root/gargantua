import logging

import uvicorn

from .routes import app


def start_fastapi_server():
    uvicorn.run(app, host="127.0.0.1", port=8000)
