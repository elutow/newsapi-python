from typing import Dict, Any

from requests import Request
from requests.auth import AuthBase


class NewsApiAuth(AuthBase):
    # Provided by newsapi: https://newsapi.org/docs/authentication
    def __init__(self, api_key: str):
        self.api_key = api_key

    def __call__(self, request: Request) -> Request:
        request.headers.update(get_auth_headers(self.api_key))
        return request


def get_auth_headers(api_key: str) -> Dict[str, Any]:
    return {
        'Content-Type': 'Application/JSON',
        'Authorization': api_key
    }
