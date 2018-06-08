"""
    Function with a List Input, removing Duplicates

    use List
"""


def remove_duplicates(list):

    value_list = []

    for num in list:
        if num not in value_list:
            value_list.append(num)

    return value_list


def main():
    print(remove_duplicates([1, 2, 2, 4, 3, 3, 2]))


main()
