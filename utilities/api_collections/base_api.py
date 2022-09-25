import requests

from utilities.decorators import auto_steps
from utilities.project_logger import logger, set_logger
from utilities.read_run_settings import ReadConfig


@auto_steps
class BaseAPI:

    def __init__(self):
        self.base_url = ReadConfig.get_api_base_url()
        self.requests = requests
        self.requests.session().cookies.clear()
        self.headers = {}
        self.url = ""
        set_logger()

    def get(self, url, body=None, headers=None, params=None):
        logger.info(f'\n{"-" * 10}GET API{"-" * 10}')
        if headers is None:
            headers = self.headers
        response = self.requests.get(f"{self.base_url}{url}", data=body, headers=headers, params=params)
        logger.info(f'\nRESPONSE {response.status_code}\nresponse text: {response.text}')
        return response

    def post(self, url, body=None, headers=None, files=None, **kwargs):
        logger.info(f'\n{"-" * 10}POST API{"-" * 10}')
        if headers is None:
            headers = self.headers
        response = self.requests.post(f"{self.base_url}{url}", data=body, headers=headers, files=files, **kwargs)
        logger.info(f'\nRESPONSE {response.status_code}\nresponse text: {response.text}')
        return response

    def delete(self, url, headers=None):
        if headers is None:
            headers = self.headers
        response = self.requests.delete(f"{self.base_url}{url}", headers=headers)
        return response

    def put(self, url, body=None, headers=None):
        if headers is None:
            headers = self.headers
        response = self.requests.put(f"{self.base_url}{url}", data=body, headers=headers)
        return response
