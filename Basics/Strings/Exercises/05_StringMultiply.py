"""
    get a string which is n (non-negative integer) copies of a given string
"""


class StringMultiple:

    def __init__(self, str, times):

        self._str = str
        self._times = times

    def multiply_string(self):

        str = self._str
        times = self._times

        if (times >= 0):
            str = str * self._times
        else:
            print('Only non-negative Values allowed!')

        print(str)


def main():

    str = input('Enter a String : ')
    timesInput = input('How many Times to multiply : ')

    times = int(timesInput)

    string_multiply = StringMultiple(str, times)

    string_multiply.multiply_string()


main()
