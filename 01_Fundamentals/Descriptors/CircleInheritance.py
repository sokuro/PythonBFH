class Widget(object):
    copyright = 'Yacrol, GmbH'


"""
    Using simple Inheritance
"""
class Circle(Widget):
    PI = 3.14

    def __init__(self, radius):
        self._radius = radius

    @property
    def circumference(self):
        return 2 * self._radius * self.PI


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

    """
        Value of the inherited Attribute
    """
    print(mycircle.copyright)

    """
        mro(): Method Resolution Order
    """
    # print(type(mycircle).mro())

    """
        Value of the Circumference
    """
    print(mycircle.circumference)

main()
