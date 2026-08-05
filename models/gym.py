class Gym:
    def __init__(self, gym_id: str, name: str, address: str, phone: str, opening_time: str, closing_time: str):
        self.gym_id = gym_id
        self.name = name
        self.address = address
        self.phone = phone
        self.opening_time = opening_time
        self.closing_time = closing_time

    def __str__(self):
        return f"[{self.gym_id}] {self.name}"



