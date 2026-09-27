
class ExerciseService:

    def __init__(self, exercise_repository):
        self.exercise_repository = exercise_repository

    def add_exercise(self, exercise):
        return self.exercise_repository.add(exercise)

    def list_exercises(self):
        return self.exercise_repository.get_all()