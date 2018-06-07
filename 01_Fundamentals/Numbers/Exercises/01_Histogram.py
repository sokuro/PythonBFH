"""
    create a histogram from a given list of integers
"""


def build_histogram(list):

    for n in list:

        result = ''

        times = n

        while times > 0:

            result += '*'
            times -= 1

        print(result)


print(build_histogram([1, 2, 3, 4]))
print(build_histogram([2, 3, 7]))
