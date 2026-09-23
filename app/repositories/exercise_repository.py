import json
from pathlib import Path
from app.model.exercises import Exercise

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class ExerciseRepository:

    def __init__(self):
        self.file_path = BASE_DIR / "data" / "exercises.json"

    def _load(self):
        with open(self.file_path, "r", encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)
        return data

    def _save(self, data):
        with open(self.file_path, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)

    def add(self, exercise):
        data = self._load()
        data.append({
            "name": exercise.name,
            "category": exercise.category,
            "description": exercise.description
        })
        self._save(data)

    def get_all(self):
        data = self._load()
        exercises = []

        for item in data:
            exercise = Exercise(
                item["name"],
                item["category"],
                item["description"]
            )
            exercises.append(exercise)

        return exercises