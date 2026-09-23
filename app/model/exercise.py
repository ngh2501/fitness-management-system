
class Exercise:
    def __init__(self, name, category, description):
        self._name = name
        self._category = category
        self._description = description

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value


