from api_testing.entities.booking import Booking


def test_create_booking(booking_service, booking):
    post_booking = booking_service.post_booking(booking)
    actual_booking = Booking(
            post_booking.json()["booking"]["firstname"],
            post_booking.json()["booking"]["lastname"],
            post_booking.json()["booking"]["totalprice"],
            post_booking.json()["booking"]["depositpaid"],
            post_booking.json()["booking"]["bookingdates"],
            post_booking.json()["booking"]["additionalneeds"])
    assert actual_booking == booking


def test_check_getting_booking_1(booking_service):
    received_response = booking_service.get_booking(1)
    keys = ["firstname",
            "lastname",
            "totalprice",
            "depositpaid",
            "bookingdates",
            ]
    assert all(key in received_response.json() for key in keys)


def test_check_getting_all_bookings(booking_service):
    received_response = booking_service.get_all_bookings()
    assert received_response.status_code == 200

