
class MembershipService:
    def __init__(self, membership_repository):
        self.membership_repository = membership_repository

    def add_membership(self, membership):
        return self.membership_repository.add(membership)

    def list_memberships(self):
        return self.membership_repository.get_all()

    def list_active_memberships(self):
        memberships = self.membership_repository.get_all()
        active_memberships = []

        for membership in memberships:
            if not membership.is_expired():
                active_memberships.append(membership)

        return active_memberships

