class Coach:
    def __init__(self,
                 coach_id: str,
                 full_name: str,
                 gender: str,
                 phone: str,
                 email: str,
                 specialization: str,
                 level: str,
                 certification: str,
                 price: int,
                 availability: str,
                 status: str = "Active"):
        self.coach_id = coach_id
        self.full_name = full_name
        self.gender = gender
        self.phone = phone
        self.email = email
        self.specialization = specialization
        self.level = level
        self.certification = certification
        self.price = price
        self.availability = availability
        self.status = status

    def __str__(self):
        return f"Coach: {self.full_name}"