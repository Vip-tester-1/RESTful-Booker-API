import pytest
from utils.auth import get_token

def test_authentication_success():
    token = get_token()
    assert token is not None
    assert isinstance(token, str)

def test_authentication_failure():
    from utils.request_handler import post_request
    url = "https://restful-booker.herokuapp.com/auth"
    payload = {"username": "invalid", "password": "wrong"}
    response = post_request(url, payload)
    assert response.status_code == 200
    assert "token" not in response.json()
