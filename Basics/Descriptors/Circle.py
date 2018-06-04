class Circle(object):
    PI = 3.14

    def __init__(self, radius):
        self._radius = radius


def main():
    mycircle = Circle(2)

    """
        Value of the Class Attribute
    """
    print(mycircle.PI)


    """
         Value stored in a dict on the Object:
         mycircle.__dict__
         {'_radius': 2}
    """
    print(mycircle._radius)

    print(type(mycircle).mro())


main()
