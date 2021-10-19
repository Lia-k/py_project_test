import json

from api_testing.app import config
from requests import Response, get, post


class BookingService:
    def __init__(self):
        self.__booking_url = f"{config['host']}/booking"

    def get_all_bookings(self) -> Response:
        return get(f"{self.__booking_url}")

    def get_booking(self, id: int) -> Response:
        return get(f"{self.__booking_url}/{id}")

    def post_booking(self, booking) -> Response:
        return post(f"{self.__booking_url}",
                    data=json.dumps(booking.__dict__),
                    headers={'Content-Type': 'application/json'})
