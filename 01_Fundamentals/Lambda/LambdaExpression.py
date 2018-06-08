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

    """
        measure call time of the Function with 'timeit'
    """
    import timeit
    # print(func(1, 2, 3))
    print(timeit.timeit('func(1, 2, 3)', setup='from __main__ import func'))

    print('\n')

    # print(f(1, 2, 3))
    print(timeit.timeit('f(1, 2, 3)', setup='from __main__ import f'))


main()
