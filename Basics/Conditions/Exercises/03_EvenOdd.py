"""
    find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
"""


class EvenOdd:

    def __init__(self, n):
        self._n = n

    def is_even_odd(self):

        n = self._n

        if n % 2 == 0:
            print('The Number', n, 'is even!')
        else:
            print('The Number', n, 'is odd!')


def main():

    check_input = input('Enter a Number : ')

    input_number = int(check_input)

    check_number = EvenOdd(input_number)

    check_number.is_even_odd()


main()
