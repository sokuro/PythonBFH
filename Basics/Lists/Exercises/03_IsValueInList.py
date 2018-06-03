"""
    check whether a specified value is contained in a group of values
"""


def is_value_in_list(list, number):

    return number in list


print(is_value_in_list([1, 2, 3, 4, 5], 6))
print(is_value_in_list([1, 2, 3, 4, 5], 3))
