"""
    Filter returns an Iterator that produces the Items Xi from the Iterator X for which the predicate p(Xi) is true
"""


""" keep only even Elements in a List """
l = list(range(5))


# With Loop
def filter_evens():

    list_even = []

    for num in l:
        if num % 2 == 0:
            list_even.append(num)

    return list_even


# filter with Lambda
def filter_lambda():
    return list(filter(lambda x: x % 2 == 0, l))


# elegant using anonymous lambda
f = list(filter(lambda x: x % 2 == 0, l))


def main():
    print(filter_evens())
    print(filter_lambda())
    print(f)


main()
