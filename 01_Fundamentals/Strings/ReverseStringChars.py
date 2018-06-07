"""
    reverse a given String
"""


class ReverseStringChars:

    def __init__(self, str):
        self._str = str

    def reverse_string(self):

        str = self._str

        print(str[::-1])


def main():

    string_input = input('Enter a String : ')

    reverse_string = ReverseStringChars(string_input)

    reverse_string.reverse_string()


main()
