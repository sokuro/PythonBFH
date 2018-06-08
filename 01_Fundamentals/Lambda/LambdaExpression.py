"""
    Simple Function Sum
"""


def func(x, y, z):
    return x + y + z


"""
    Same Function with Lambda Expression
"""


f = lambda x, y, z: x + y + z


def main():
    print(func(1, 2, 3))
    print(f(1, 2, 3))


main()
