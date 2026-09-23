from app.repositories.workout_repository import WorkoutRepository


class WorkoutService:

    def __init__(self):
        self.repository = WorkoutRepository()

    def add_workout(self, workout):
        self.repository.add(workout)

    def get_all_workouts(self):
        return self.repository.get_all()
