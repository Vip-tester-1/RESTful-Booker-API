from utils.request_handler import post_request, put_request
from utils.auth import get_token
from data.booking_data import valid_booking_data, updated_booking_data

def test_update_booking():
    # Step 1: Create a booking
    create_url = "https://restful-booker.herokuapp.com/booking"
    create_response = post_request(create_url, valid_booking_data)
    assert create_response.status_code == 200
    booking_id = create_response.json()["bookingid"]

    # Step 2: Update the created booking
    token = get_token()
    update_url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={token}"
    }

    update_response = put_request(update_url, updated_booking_data, headers=headers)
    assert update_response.status_code == 200
    assert update_response.json()["firstname"] == updated_booking_data["firstname"]

