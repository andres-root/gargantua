from abc import ABC, abstractmethod


class HttpRequestOutputPort(ABC):
    @abstractmethod
    def get(self, url: str, method: str, payload: dict) -> dict:
        raise NotImplementedError

    @abstractmethod
    def post(self, url: str, method: str, payload: dict):
        raise NotImplementedError
