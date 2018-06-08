"""
    Class: PositiveAttribute Descriptor
    Negative Attributes of the Class 'Person' are not allowed!
"""


class PositiveAttribute:

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            # raise ValueError('Cannot be negative!')
            if self.name == 'age':
                raise ValueError('Age can not be negative!')
            elif self.name == 'salary':
                raise ValueError('Salary can not be negative!')
        instance.__dict__[self.name] = value


"""
    Class: Person
    Attributes: age, salary
"""


class Person:

    # implementing the Descriptor
    age = PositiveAttribute('age')
    salary = PositiveAttribute('salary')

    def __init__(self, name, age, salary):

        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return 'Person({}, {}, {})'.format(self.name, self.age, self.salary)


def main():
    import doctest
    # doctest.testmod()

    bob = Person('Alice Brown', 42, 123000)
    print(bob.__repr__())

    charlie = Person('Charlie Davis', -1, 5000)
    print(charlie.__repr__())

    charlie = Person('Fox Mulder', 57, -5000)
    print(charlie.__repr__())


main()
