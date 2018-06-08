"""
    Function to sum all Numbers in the List

    use a List
"""


def sum_numbers(numbers):

    sum = 0

    for num in numbers:
        sum += num

    return sum


def main():

    print(sum_numbers([1, 2, 3]))   # list

    print(sum_numbers((1, 2, 3)))   # tuple


main()
