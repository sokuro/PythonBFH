"""
    Function to sum all Numbers in the List

    use *args
"""


def sum_numbers(*args):

    sum = 0

    for num in args:
        sum += num

    return sum


def main():
    print(sum_numbers(1, 2, 3))


main()
