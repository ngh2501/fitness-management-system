from models.coach import Coach


class CoachManager:

    def __init__(self):
        self.coaches: list[Coach] = []

    def add_coach(self, coach: Coach):
        self.coaches.append(coach)

    def get_all_coaches(self):
        return self.coaches

    def find_coach_by_id(self, coach_id: str):
        for coach in self.coaches:
            if coach.coach_id == coach_id:
                return coach
        return None

    def deactivate_coach(self, coach_id: str) -> bool:
        coach = self.find_coach_by_id(coach_id)

        if coach:
            coach.status = "Inactive"
            return True
        return False

    def update_coach(self, updated_coach: Coach) -> bool:
        coach = self.find_coach_by_id(updated_coach.coach_id)

        if not coach:
            return False

        coach.full_name = updated_coach.full_name
        coach.gender = updated_coach.gender
        coach.phone = updated_coach.phone
        coach.email = updated_coach.email
        coach.specialization = updated_coach.specialization
        coach.level = updated_coach.level
        coach.certification = updated_coach.certification
        coach.price = updated_coach.price
        coach.availability = updated_coach.availability

        return True