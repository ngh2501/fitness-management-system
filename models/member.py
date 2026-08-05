class Member:
    def __init__(self, member_id: str, full_name: str, gender: str, phone: str, email: str, membership_type: str, status: str = "Active"):
        self.member_id = member_id
        self.full_name = full_name
        self.gender = gender
        self.phone = phone
        self.email = email
        self.membership_type = membership_type
        self.status = status

    def __str__(self):
        return f"Member: {self.full_name}"