from utilities.api_collections.mock_server_api.mock_server_api import MockServerApi
from http import HTTPStatus


class TestMockServerApi:

    def test_get_api(self):
        """

        """
        response = MockServerApi().mock_get()
        assert response.status_code == HTTPStatus.OK, f'Status code is not as expected' \
                                                      f'\nActual: {response.status_code}' \
                                                      f'\nExpected: {HTTPStatus.OK}'

    def test_post_api(self):
        """

        """
        response = MockServerApi().mock_post()
        assert response.status_code == HTTPStatus.OK, f'Status code is not as expected' \
                                                      f'\nActual: {response.status_code}' \
                                                      f'\nExpected: {HTTPStatus.OK}'

    def test_put_api(self):
        """

        """
        response = MockServerApi().mock_put()
        assert response.status_code == HTTPStatus.OK, f'Status code is not as expected' \
                                                      f'\nActual: {response.status_code}' \
                                                      f'\nExpected: {HTTPStatus.OK}'

    def test_delete_api(self):
        """

        """
        response = MockServerApi().mock_delete()
        assert response.status_code == HTTPStatus.OK, f'Status code is not as expected' \
                                                      f'\nActual: {response.status_code}' \
                                                      f'\nExpected: {HTTPStatus.OK}'
