from models.member import Member


class MemberManager:

    def __init__(self):
        self.members: list[Member] = []

    def add_member(self, member: Member):
        self.members.append(member)

    def deactivate_member(self, member_id: str):
        member = self.find_member_by_id(member_id)

        if member:
            member.status = "Inactive"
            return True
        return False

    def get_all_members(self):
        return self.members

    def find_member_by_id(self, member_id: str):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def update_member(self, updated_member: Member):
        member = self.find_member_by_id(updated_member.member_id)

        if not member:
            return False

        member.full_name = updated_member.full_name
        member.phone = updated_member.phone
        member.email = updated_member.email
        member.membership_type = updated_member.membership_type

        return True