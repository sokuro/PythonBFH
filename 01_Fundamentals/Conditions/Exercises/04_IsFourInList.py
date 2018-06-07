"""
    count the number 4 in a given list
"""


def is_four_in_list(list):

    count = 0

    for num in list:

        if num == 4:
            count += 1

    return count


print('The number 4 is in the list', is_four_in_list([1, 2, 3, 4, 5]), 'times')
print('The number 4 is in the list', is_four_in_list([1, 2, 3, 4, 4]), 'times')

