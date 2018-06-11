"""
    Inheritance of an Employee -> Person
"""


# Main Class
class Person:

    def __init__(self, first, last, age):

        self.first_name = first
        self.last_name = last
        self.age = age

    def __str__(self):

        return self.first_name + " " + self.last_name + " " + str(self.age)


# Inherited Class
class Employee(Person):

    def __init__(self, first, last, age, staff_number):
        super().__init__(first, last, age)
        self._staff_number = staff_number

    def __str__(self):

        return super().__str__() + ", " + str(self._staff_number)


def main():

    x = Person("Marge", "Simpson", 36)

    y = Employee("Karol", "Ugorcak", 37, 101)

    print(x)

    print(y)


main()
