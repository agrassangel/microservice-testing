from dataclasses import dataclass
from test.common.config import BASE_URI
from requests.auth import HTTPBasicAuth
import requests
import pytest


@dataclass
class Response:
    status_code: int
    text: str
    json_r: object
    headers: dict


class LocalRequest:

    def __init__(self):
        self.session = requests.Session()
        self.url = BASE_URI
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.current_path = ''

    def get(self, path, **kwargs):
        self.current_path = path
        response = self.session.get(self.url + path, **kwargs)
        return self.__get_responses(response)

    def post(self, path, payload, headers=None, **kwargs):
        self.current_path = path
        response = self.session.post(self.url + path, data=payload,
                                     headers=headers if headers is not None else self.headers, **kwargs)
        return self.__get_responses(response)

    def delete(self, path, **kwargs):
        self.current_path = path
        response = self.session.delete(self.url + path, **kwargs)
        return self.__get_responses(response)

    def login(self, path, username, password):
        return self.get(path, auth=HTTPBasicAuth(username, password))

    def clear_cookies_from_session(self):
        self.session.cookies.clear()

    def get_current_path(self):
        return self.current_path

    def valid_status_code(self):
        return requests.codes.ok

    def __get_responses(self, response):
        status_code = response.status_code
        text = response.text

        try:
            json_r = response.json()
        except Exception:
            json_r = {}

        headers = response.headers

        return Response(
            status_code, text, json_r, headers
        )


@pytest.fixture
def request_manager():
    req = LocalRequest()
    return req

# basic = HTTPBasicAuth('user', 'password')
# u = BASE_URI + '/login'
# r = requests.Session().get(u, auth=basic)
# print(r)
