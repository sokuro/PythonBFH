"""
    Function to find the Max of 3 Numbers

    use Recursion
"""


def max_two_numbers( x, y ):
    if x > y:
        return x
    return y


def max_three_numbers( x, y, z ):
    return max_two_numbers( x, max_two_numbers(y, z))


def main():
    print(max_three_numbers(1, 2, 3))


main()
