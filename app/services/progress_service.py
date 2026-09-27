class ProgressService:

    def __init__(self, workout_history):
        self._workout_history = workout_history

    def calculate_weekly_volume(self):
        weekly_volume = {}

        for workout in self._workout_history:

            year, week, _ = workout.date.isocalendar()
            week_key = f"{year}-W{week}"

            if week_key not in weekly_volume:
                weekly_volume[week_key] = {}

            for exercise in workout.exercises:
                exercise_name = exercise["exercise"]
                volume = exercise["volume"]

                if exercise_name not in weekly_volume[week_key]:
                    weekly_volume[week_key][exercise_name] = 0

                weekly_volume[week_key][exercise_name] += volume

        return weekly_volume