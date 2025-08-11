from utils.request_handler import post_request, get_request
from data.booking_data import valid_booking_data

def test_get_existing_booking():
    # Step 1: Create a new booking
    create_url = "https://restful-booker.herokuapp.com/booking"
    create_response = post_request(create_url, valid_booking_data)
    assert create_response.status_code == 200
    booking_id = create_response.json()["bookingid"]

    # Step 2: Get the created booking
    get_url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    get_response = get_request(get_url)
    assert get_response.status_code == 200
    assert get_response.json()["firstname"] == valid_booking_data["firstname"]

