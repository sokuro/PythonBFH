"""
    Function with a List Input, removing Duplicates

    use *args
"""


def remove_duplicates(*args):

    value_list = []

    for num in args:
        if num not in value_list:
            value_list.append(num)

    return value_list


def main():
    print(remove_duplicates(1, 2, 3, 4, 4, 2, 5))


main()



