"""
    Compute Average

    Average: sum of Values divided by the Number of Values

    Aggregation State is a Tuple: (partial_sum, partial_count)
"""

l = [1, 4, 2, 5, 3]


def average_values():

    from functools import reduce

    agg = reduce(lambda partial_aggregation, value: (partial_aggregation[0] + value,
                                                     partial_aggregation[1] + 1),
                                                     l, (0, 0))     # (0,0) initial partial aggregate

    average = agg[0] / agg[1]

    return agg              # >> (15, 5)
    # return average        # >> 3.0


def main():

    print(average_values())


main()
