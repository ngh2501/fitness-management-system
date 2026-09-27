from app.utils.exceptions import DuplicateEmailError


class MemberService:
    def __init__(self, member_repository):
        self.member_repository = member_repository

    def register_member(self, member):
        existing_member = self.member_repository.get_by_email(member.email)
        if existing_member:
            raise DuplicateEmailError(member.email)
        return self.member_repository.add(member)


    def deactivate_member(self, member_id):
        member = self.member_repository.get_by_id(member_id)
        if member is None:
            return False
        member.is_active = False
        self.member_repository.update(member)
        return True

    def list_active_members(self):
        members = self.member_repository.get_all()
        active_members = []

        for member in members:
            if member.is_activate:
                active_members.append(member)

        return active_members