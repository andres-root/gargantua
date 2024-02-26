import logging

import requests
from requests.exceptions import RequestException

from ....ports.output.http_request import HttpRequestOutputPort


class HttpRequest(HttpRequestOutputPort):
    def __init__(self, timeout=None):
        super().__init__()
        self.timeout = timeout or 5

    def get(self, url: str, payload: dict) -> dict:
        try:
            response = requests.get(url, params=payload, timeout=self.timeout)
            response.raise_for_status()

            return response.json()
        except RequestException as e:
            logging.error(f"error getting data from {url}: {e}")
            raise Exception(f"error getting data from {url}: {e}")
