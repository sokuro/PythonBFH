"""
    calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
"""


class SumThreeNumbers:

    def __init__(self, x, y, z):

        # instance Variables
        self._x = x
        self._y = y
        self._z = z

    def calculate_sum(self):

        x = self._x
        y = self._y
        z = self._z

        sum = x + y + z

        if x == y == z:
            sum = sum * 3

        print(sum)


def main():

    intInput = input('Input 3 Integers : ')

    # Build a List from the Input
    list = intInput.split(' ')

    # convert to Integer
    x = int(list[0])
    y = int(list[1])
    z = int(list[2])

    callClass = SumThreeNumbers(x, y, z)

    callClass.calculate_sum()


""" call the Main Method """
main()
