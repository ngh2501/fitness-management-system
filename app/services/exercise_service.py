from app.repositories.exercise_repository import ExerciseRepository


class ExerciseService:

    def __init__(self):
        self.repository = ExerciseRepository()

    def add_exercise(self, exercise):
        self.repository.add(exercise)

    def get_all_exercises(self):
        return self.repository.get_all()
