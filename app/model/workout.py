

class Workout:
    def __init__(self, workout_id, _member_id, _date):
        self._workout_id = workout_id
        self._member_id = _member_id
        self._date = _date
        self._exercises = []

    def add_exercise(self, exercise, sets, reps, weight):
        exercise_data = {
            "exercise": exercise,
            "sets": sets,
            "reps": reps,
            "weight": weight,
            "volumn": sets * reps * weight
        }
        self._exercises.append(exercise_data)
