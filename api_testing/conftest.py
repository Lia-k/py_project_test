import pytest

from api_testing.entities.booking import Booking
from api_testing.infrastructure.booking_service import BookingService


@pytest.fixture(scope="session")
def booking_service():
    yield BookingService()


@pytest.fixture()
def booking():
    yield Booking(
        firstname="Sally1",
        lastname="Brown1",
        totalprice=447,
        depositpaid=False,
        bookingdates={'checkin': '2016-04-16',
                      'checkout': '2020-11-22'},
        additionalneeds="Dinner"
    )
