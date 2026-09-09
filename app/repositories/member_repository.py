import json
from app.model.Member import Member


class MemberRepository:

    def __init__(self):
        self.file_path = "data/members.json"

    def _load(self):
        with open(self.file_path) as jsonfile:
            data = json.load(jsonfile)
        return data

    def _save(self, data):
        with open(self.file_path, "w") as jsonfile:
            json.dump(data, jsonfile)

    def add(self, member):
        data = self._load()
        data.append(member.to_dict())
        self._save(data)

    def get_all(self):
        data = self._load()
        tatcamember = []
        for member in data:
            member = Member.from_dict(member)
            tatcamember.append(member)
        return tatcamember

    def get_by_id(self, member_id):
        data = self._load()
        for member in data:
            member = Member.from_dict(member)
            if member.member_id == member_id:
                return member
        return None


    def get_by_email(self, email):
        data = self._load()
        for member in data:
            member = Member.from_dict(member)
            if member.email == email:
                return member
        return None

    def update(self, member):
        data = self._load()
        for i in range (len(data)):
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
