from __future__ import annotations


class Booking:
    def __init__(self,
                 firstname,
                 lastname,
                 totalprice,
                 depositpaid,
                 bookingdates,
                 additionalneeds
                 ):
        self.firstname = firstname
        self.lastname = lastname
        self.totalprice = totalprice
        self.depositpaid = depositpaid
        self.bookingdates = bookingdates
        self.additionalneeds = additionalneeds

    def __eq__(self, other: Booking):
        return self.__dict__ == other.__dict__
