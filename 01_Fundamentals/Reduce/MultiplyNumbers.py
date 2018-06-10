"""
    Multiply all Numbers in a List
"""


data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


# using loop
def multiply_with_loop(data):

    product = 1

    for num in data:
        product *= num

    return product


# using multiplier
def multiply_numbers():

    return lambda x, y: x * y


# using reduce
def multiply_reduce(data):

    from functools import reduce

    return reduce(multiply_numbers(), data)


def main():

    print(multiply_with_loop(data))
    print(multiply_reduce(data))


main()
