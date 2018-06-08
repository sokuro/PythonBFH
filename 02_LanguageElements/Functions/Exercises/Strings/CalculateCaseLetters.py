"""
    Function that accepts a string and calculate the number of upper case letters and lower case letters.

    Use Dictionary with 2 keys:
        > upper Case Letters
        > lower Case Letters
"""


def calculate_letters(str):

    d = {"upper_case": 0, "lower_case": 0}

    for char in str:

        if char.isupper():
            d["upper_case"] += 1

        elif char.islower():
            d["lower_case"] += 1

        else:
            pass

    print('Original String: ', str)
    print('Upper Case Letters: ', d["upper_case"])
    print('Lower Case Letters: ', d["lower_case"])

    print(d.items())
    # >> dict_items([('upper_case', 2), ('lower_case', 8)])


def main():
    calculate_letters('Lorem Ipsum')


main()