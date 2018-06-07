"""
    reverse words in a string
"""


class ReverseStringWords:

    def __init__(self, str):
        self._str = str

    def reverse_string(self):

        str = self._str

        for word in str.split('\n'):
            print(' '.join(word.split()[::-1]))


def main():

    string_input = input('Enter a String : ')

    reverse_string = ReverseStringWords(string_input)

    reverse_string.reverse_string()


main()
