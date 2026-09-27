class WorkoutService:

    def __init__(self, workout_repository):
        self.workout_repository = workout_repository

    def add_workout(self, workout):
        return self.workout_repository.add(workout)

    def list_workouts(self):
        return self.workout_repository.get_all()