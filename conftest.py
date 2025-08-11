import pytest
import json
from utils.auth import get_token

# Load config once at the beginning of the test session
@pytest.fixture(scope="session")
def config():
    with open("config/config.json") as config_file:
        return json.load(config_file)

# Fixture to provide base URL
@pytest.fixture(scope="session")
def base_url(config):
    return config["base_url"]

# Fixture to provide an authentication token
@pytest.fixture(scope="session")
def auth_token():
    token = get_token()
    if not token:
        pytest.fail("Authentication failed. Could not retrieve token.")
    return token

# Fixture to construct common headers for authorized requests
@pytest.fixture
def auth_headers(auth_token):
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={auth_token}"
    }
