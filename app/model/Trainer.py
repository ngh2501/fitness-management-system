from app.model.person import Person
class Trainer(Person):
    def __init__(self, name, email, phone, birth,
                 trainer_id, specialty,
                 experience__year):
        super().__init__(name, email, phone, birth)
        self.trainer_id = trainer_id
        self.specialty = specialty
        self.experience__year = experience__year
        self.assigned_member = []

    def get_role(self):
        return "Trainer"

    def assign_member(self, member):
        self.assigned_member.append(member)

    def get_member_count(self):
        return len(self.assigned_member)

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["email"],
            data["phone"],
            data["birth"],
            data["trainer_id"],
            data["specialty"],
            data["experience__year"]
        )

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self._phone,
            "birth": self._birth,
            "trainer_id": self.trainer_id,
            "specialty": self.specialty,
            "experience__year": self.experience__year
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["email"],
            data["phone"],
            data["birth"],
            data["trainer_id"],
            data["specialty"],
            data["experience__year"]
        )