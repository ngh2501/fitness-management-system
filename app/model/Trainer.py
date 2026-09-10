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