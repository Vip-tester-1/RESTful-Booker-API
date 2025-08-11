from utils.request_handler import post_request, delete_request
from utils.auth import get_token
from data.booking_data import valid_booking_data

def test_delete_booking():
    # Step 1: Create a booking
    create_url = "https://restful-booker.herokuapp.com/booking"
    create_response = post_request(create_url, valid_booking_data)
    assert create_response.status_code == 200
    booking_id = create_response.json()["bookingid"]

    # Step 2: Get token
    token = get_token()
    assert token is not None

    # Step 3: Delete the booking
    delete_url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }

    delete_response = delete_request(delete_url, headers=headers)

    # Step 4: Validate response
    assert delete_response.status_code in [200, 201, 204]

