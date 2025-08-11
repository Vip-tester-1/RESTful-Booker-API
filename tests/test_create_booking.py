from utils.request_handler import post_request
from data.booking_data import valid_booking_data

def test_create_booking():
    url = "https://restful-booker.herokuapp.com/booking"
    response = post_request(url, valid_booking_data)
    assert response.status_code == 200
    assert "bookingid" in response.json()


