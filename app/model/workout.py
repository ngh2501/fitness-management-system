class Workout:
    def __init__(self, workout_id, member_id, date):
        self._workout_id = workout_id
        self._member_id = member_id
        self._date = date
        self._exercises = []

    @property
    def date(self):
        return self._date

    @property
    def exercises(self):
        return self._exercises

    @property
    def workout_id(self):
        return self._workout_id

    @property
    def member_id(self):
        return self._member_id

    def add_exercise(self, exercise, sets, reps, weight):
        exercise_data = {
            "exercise": exercise,
            "sets": sets,
            "reps": reps,
            "weight": weight,
            "volume": sets * reps * weight
        }

        self._exercises.append(exercise_data)

    def to_dict(self):
        return {
            "workout_id": self._workout_id,
            "member_id": self._member_id,
            "date": self._date,
            "exercises": self._exercises
        }

    @classmethod
    def from_dict(cls, data):
        workout = cls(
            data["workout_id"],
            data["member_id"],
            data["date"]
        )

        workout._exercises = data["exercises"]

        return workout