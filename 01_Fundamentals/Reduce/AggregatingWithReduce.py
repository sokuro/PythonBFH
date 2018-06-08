"""
    Elements from Iterables can be reduced to an aggregated Value

    max(iterable): returns the largest Value in the Iterable
    min(iterable): returns the smallest Value in the Iterable
    sum(iterable): returns the sum of all Values in the Iterable

    reduce(function, iterable)
"""


"""
    Aggregate: ((((1 + 4) + 2) + 5) + 3)
"""

l = [1, 4, 2, 5, 3]


# Aggregate via reduce with Lambda
def reduce_from_list():

    from functools import reduce

    f = lambda x, y: x + y

    s = reduce(f, l)

    return s


# using the build-in add Operator
def reduce_simpler():

    from functools import reduce
    import operator

    s = reduce(operator.add, l)

    return s


# simplest Version using Sum
def reduce_sum():

    return sum(l)


def main():
    print(reduce_from_list())
    print(reduce_simpler())
    print(reduce_sum())


main()
