from app.model.person import Person

class Member(Person):
    def __init__(self, name, email, phone, birth, member_id, is_activate=True):
        super().__init__(name, email, phone, birth)
        self.member_id = member_id
        self.is_activate = is_activate
        self._workout_history = []

    def __str__(self):
        return f"Member: {self.name} ({self.email})"

    def get_role(self):
        return "Member"

    def activate(self):
        self.is_activate = True

    def deactivate(self):
        self.is_activate = False

    def add_workout(self, workout):
        self._workout_history.append(workout)

    def to_dict(self):
        return {
            "name": getattr(self, "name", getattr(self, "_name", None)),
            "email": getattr(self, "email", getattr(self, "_email", None)),
            "phone": getattr(self, "phone", getattr(self, "_phone", None)),
            "birth": getattr(self, "birth", getattr(self, "_birth", None)),
            "member_id": self.member_id,
            "is_activate": self.is_activate
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["email"],
            data["phone"],
            data["birth"],
            data["member_id"],
            data["is_activate"]
        )

    def __repr__(self):
        name = getattr(self, "name", getattr(self, "_name", ""))
        email = getattr(self, "email", getattr(self, "_email", ""))
        return f"Member(id='{self.member_id}', name='{name}', email='{email}')"



