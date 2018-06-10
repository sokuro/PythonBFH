"""
    Filter average from a List
"""


data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# calculate average
def calculate_average(data):

    import statistics

    avg = statistics.mean(data)

    return avg


# filter Elements greater than the Average
def filter_greater(data):

    avg = calculate_average(data)

    return list(filter(lambda x: x > avg, data))


# filter Element smaller than the Average
def filter_smaller(data):

    avg = calculate_average(data)

    return list(filter(lambda x: x < avg, data))


def main():

    print(calculate_average(data))
    print(filter_greater(data))
    print(filter_smaller(data))


main()




