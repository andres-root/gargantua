from abc import ABC, abstractmethod


class FetchDataInputPort(ABC):
    @abstractmethod
    def fetch_data(self, input_id: str):
        raise NotImplementedError


class SaveDataInputPort(ABC):
    @abstractmethod
    def save_data(self, input_id: str, data: dict):
        raise NotImplementedError


class RetrieveDataInputPort(ABC):
    @abstractmethod
    def retrieve_data(self, input_id: str):
        raise NotImplementedError
