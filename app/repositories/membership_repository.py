import json
from pathlib import Path
from datetime import date
from app.model.membership import Membership

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class MembershipRepository:

    def __init__(self):
        self.file_path = BASE_DIR / "data" / "memberships.json"

    def _load(self):
        with open(self.file_path, "r", encoding="utf-8") as jsonfile:
            return json.load(jsonfile)

    def _save(self, data):
        with open(self.file_path, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)

    def add(self, membership):
        data = self._load()

        data.append({
            "type": membership.membership_type,
            "start_date": membership.start_date.isoformat(),
            "end_date": membership.end_date.isoformat(),
            "price": membership.price
        })

        self._save(data)

    def get_all(self):
        data = self._load()
        memberships = []

        for item in data:
            membership = Membership(
                item["type"],
                date.fromisoformat(item["start_date"]),
                date.fromisoformat(item["end_date"]),
                item["price"]
            )
            memberships.append(membership)

        return memberships