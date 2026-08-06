from models.booking import Booking


class BookingManager:

    def __init__(self):
        self.bookings: list[Booking] = []

    def add_booking(self, booking: Booking):
        self.bookings.append(booking)

    def get_all_bookings(self):
        return self.bookings

    def find_booking_by_id(self, booking_id: str):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                return booking
        return None

    def cancel_booking(self, booking_id: str) -> bool:
        booking = self.find_booking_by_id(booking_id)

        if booking:
            booking.status = "Cancelled"
            return True
        return False

    def update_booking(self, updated_booking: Booking) -> bool:
        booking = self.find_booking_by_id(updated_booking.booking_id)

        if not booking:
            return False

        booking.member = updated_booking.member
        booking.coach = updated_booking.coach
        booking.service = updated_booking.service
        booking.booking_date = updated_booking.booking_date
        booking.slot = updated_booking.slot
        booking.status = updated_booking.status

        return True