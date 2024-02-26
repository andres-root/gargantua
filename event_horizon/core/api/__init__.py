class Api:
    def __init__(self, client):
        self.client = client

    def get_data(self, url, payload):
        return self.client.get(url, payload)
