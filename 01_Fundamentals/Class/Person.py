"""
    Simple Class to display the main Parts of a Class
"""


class Person:

    """" Instantiation """
    def __init__(self, name):
        self._name = name

    """ Method  """
    def greet_multiple_times(self, times):
        for _ in range(times):
            print(f'Hello {self._name}')


def main():

    """ create a Person Object """
    bob = Person('Bob')

    bob.greet_multiple_times(5)


main()