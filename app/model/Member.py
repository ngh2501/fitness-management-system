from app.model.Person import Person

class Member(Person):
    def __init__(self, name, email, phone, birth, member_id, is_activate=True):
        super().__init__(name, email, phone, birth)
        self.member_id = member_id
        self.is_activate = is_activate
        self._workouts = []

    def get_role(self):
        return "Member"

    def activate(self):
         self.is_activate = True

    def deactivate(self):
         self.is_activate = False

    def add_workout(self,workout):
         self._workouts.append(workout)

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['name'],
            data['email'],
            data['phone'],
            data['birth'],
            data['member_id'],
            data['is_activate']
        )





