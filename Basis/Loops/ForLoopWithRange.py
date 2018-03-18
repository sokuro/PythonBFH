"""
* xrange was replaced by range and xrange was removed!
"""


class ForIterationWithRange:

    n_max = 10
    s = 0

    for i in range(1, n_max + 1):
        s += i
    print(s)                            # >> 55