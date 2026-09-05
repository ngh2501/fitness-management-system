from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name, email, phone, birth):
        self.name = name
        self.email = email
        self._phone = phone
        self._birth = birth

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Tên không được để trống")
        self._name = value.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value.strip():
            raise ValueError("Email phải chứa @")
        self._email = value.strip()

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return f"{self.get_role()}: {self._name} ({self._email})"