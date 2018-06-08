"""
    Class: Descriptor: Name of a Person

    Access the Descriptor like it is an Instance Variable
"""


class Name:

    def __get__(self, instance, owner):
        print('Fetch Name of a Person...')
        return instance._name

    def __set__(self, instance, value):
        print('Change Name of a Person...')
        instance._name = value

    def __delete__(self, instance):
        print('Remove Name of a Person...')
        del instance._name


"""
    Class: Person
"""


class Person:

    def __init__(self, name):
        self._name = name

    name = Name()           # Assign Descriptor to Attribute


def main():

    bob = Person('Bob Smith')
    print(bob.name)             # executes Name.__get__

    bob.name = 'Robert Smith'   # executes Name.__set__
    print(bob.name)


main()