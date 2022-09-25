from utilities.api_collections.base_api import BaseAPI
from utilities.decorators import auto_steps


@auto_steps
class MockServerApi(BaseAPI):
    def __init__(self):
        super().__init__()
        self.url = '/api/'

    def mock_get(self, body=None, headers=None, params=None):
        response = self.get(url=f'{self.url}/get')
        return response

    def mock_post(self, body=None, headers=None, files=None, **kwargs):
        response = self.post(url=f'{self.url}/post')
        return response

    def mock_put(self, body=None, headers=None):
        response = self.put(url=f'{self.url}/put')
        return response

    def mock_delete(self, headers=None):
        response = self.delete(url=f'{self.url}/delete')
        return response
