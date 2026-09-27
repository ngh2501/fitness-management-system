import json
from pathlib import Path
from app.model.workout import Workout

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class WorkoutRepository:

    def __init__(self):
        self.file_path = BASE_DIR / "data" / "workouts.json"

    def _load(self):
        with open(self.file_path, "r", encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)
        return data

    def _save(self, data):
        with open(self.file_path, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)

    def add(self, workout):
        data = self._load()
        data.append(workout.to_dict())
        self._save(data)

    def get_all(self):
        data = self._load()
        workouts = []

        for item in data:
            workout = Workout.from_dict(item)
            workouts.append(workout)

        return workouts