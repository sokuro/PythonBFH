"""
    Function to Map Digit Names
"""


def generate_digits():

    import random

    num_digits = 5
    # 1) generate 5 random Digits (0:9)
    random_digits = map(lambda _: random.randint(0, 9), range(num_digits))

    # 2) Dictionary of the digit Names
    digit_names = {0: 'zero',
                   1: 'one',
                   2: 'two',
                   3: 'three',
                   4: 'four',
                   5: 'five',
                   6: 'six',
                   7: 'seven',
                   8: 'eight',
                   9: 'nine'}

    # 3) convert Digits to Name Strings
    names = map(lambda digit: digit_names[digit], random_digits)

    # 4) implement the Upper Case Helper Function
    f = upper_case_names(names)

    # 5) iterate and print the Numbers
    for num in f:
        print(num)


""" Helper Function to convert Names to upper Case """


def upper_case_names(names):
    return map(str.upper, names)


def main():

    generate_digits()


main()
