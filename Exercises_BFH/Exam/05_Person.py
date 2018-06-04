"""
    Class: Person
    Attributes: age, salary
"""


class Person:

    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary

    def __repr__(self):
        return 'Person({}, {}, {})'.format(self._name, self._age, self._salary)


"""
    Class: PositiveAttribute
    Negative Attributes of the Class 'Person' are not allowed!
"""


class PositiveAttribute:

    def __init__(self, age, salary):
        self._age = age
        self._salary = salary

    