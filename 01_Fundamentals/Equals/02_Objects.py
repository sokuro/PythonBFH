"""
    Comparing the Object
"""


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == self.age


def main():

    jack_one = Person('Jack', 23)
    jack_two = Person('Jack', 23)

    print(jack_one == jack_two)         # True

    print(jack_one is jack_two)         # False
    # NOT the same Instance of the Object


main()
