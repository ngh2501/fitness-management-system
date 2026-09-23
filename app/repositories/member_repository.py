import json
from pathlib import Path
from app.model.member import Member

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class MemberRepository:

    def __init__(self):
        self.file_path = BASE_DIR / "data" / "trainers.json"

    def _load(self):
        with open(self.file_path, "r", encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)
        return data

    def _save(self, data):
        with open(self.file_path, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)

    def add(self, member):
        data = self._load()
        data.append(member.to_dict())
        self._save(data)

    def get_all(self):
        data = self._load()
        tatcamember = []

        for item in data:
            m = Member.from_dict(item)
            tatcamember.append(m)

        return tatcamember

    def get_by_id(self, member_id):
        data = self._load()

        for item in data:
            m = Member.from_dict(item)
            if m.member_id == member_id:
                return m

        return None

    def get_by_email(self, email):
        data = self._load()

        for item in data:
            m = Member.from_dict(item)
            if m.email == email:
                return m

        return None

    def update(self, member):
        data = self._load()

        for i in range(len(data)):
            if data[i]["member_id"] == member.member_id:
                data[i] = member.to_dict()
                self._save(data)
                return True

        return False

    def delete(self, member_id):
        data = self._load()

        for i in range(len(data)):
            if data[i]["member_id"] == member_id:
                data.pop(i)
                self._save(data)
                return True

        return False