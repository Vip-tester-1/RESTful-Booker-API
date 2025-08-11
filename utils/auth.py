from utils.request_handler import post_request

def get_token():
    url = "https://restful-booker.herokuapp.com/auth"
    payload = {"username": "admin", "password": "password123"}
    response = post_request(url, payload)
    return response.json().get("token", None)
