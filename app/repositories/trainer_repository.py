import json
from pathlib import Path
from app.model.trainer import Trainer

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class TrainerRepository:

    def __init__(self):
        self.file_path = BASE_DIR / "data" / "trainers.json"

    def _load(self):
        with open(self.file_path, "r", encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)
        return data

    def _save(self, data):
        with open(self.file_path, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)

    def add(self, trainer):
        data = self._load()
        data.append(trainer.to_dict())
        self._save(data)

    def get_all(self):
        data = self._load()
        tatcatrainer = []

        for item in data:
            m = Trainer.from_dict(item)
            tatcatrainer.append(m)

        return tatcatrainer

    def get_by_id(self, trainer_id):
        data = self._load()

        for item in data:
            t = Trainer.from_dict(item)
            if t.trainer_id == trainer_id:
                return t

        return None

    def get_by_email(self, email):
        data = self._load()

        for item in data:
            t = Trainer.from_dict(item)
            if t.email == email:
                return t

        return None

    def update(self, trainer):
        data = self._load()

        for i in range(len(data)):
            if data[i]["trainer_id"] == trainer.trainer_id:
                data[i] = trainer.to_dict()
                self._save(data)
                return True

        return False

    def delete(self, trainer_id):
        data = self._load()

        for i in range(len(data)):
            if data[i]["trainer_id"] == trainer_id:
                data.pop(i)
                self._save(data)
                return True

        return False