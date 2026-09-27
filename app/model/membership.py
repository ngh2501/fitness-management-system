from datetime import date


class Membership:

    def __init__(self, member_id, membership_type, start_date, end_date, price):
        self._member_id = member_id
        self._membership_type = membership_type
        self._start_date = start_date
        self._end_date = end_date
        self._price = price

    @property
    def member_id(self):
        return self._member_id

    @property
    def membership_type(self):
        return self._membership_type

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    @property
    def price(self):
        return self._price

    def is_expired(self):
        return date.today() > self._end_date
