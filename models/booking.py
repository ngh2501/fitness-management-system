from models.member import Member
from models.coach import Coach
from models.service import Service

class Booking:
    def __init__(self,
                 booking_id: str,
                 member: Member,
                 coach: Coach,
                 service: Service,
                 booking_date: str,
                 slot: str,
                 status: str = "Pending"):
        self.booking_id = booking_id
        self.member = member
        self.coach = coach
        self.service = service
        self.booking_date = booking_date
        self.slot = slot
        self.status = status


    def __str__(self):
        return (
            f"[{self.booking_id}] "
            f"{self.member.full_name} booked "
            f"{self.service.name} "
            f"with {self.coach.full_name} "
            f"on {self.booking_date} "
            f"({self.slot})"
        )