"""
    classic Class
"""


class MyClass:

    """ instantiation Operation """
    def __init__(self, str):
        self._str = str

    """ attribute Reference """
    i = 123

    """ Method Example """
    def f(self):
        print(f'{self._str}')


""" Main Method """


def main():
    """
        create a new Instance of MyClass
    """

    """ assign the Object to a local Variable """
    greeting = MyClass('hello world')

    """ call the Method """
    greeting.f()


""" call the Main Method """
main()
