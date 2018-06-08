"""
    Function to find the Max of three numbers

    use **kwargs
"""


def max_function(**kwargs):

    value_list = []
    max_value = None

    for key, value in kwargs.items():
        if max_value is None or value > max_value:
            value_list = value
            max_value = value
        elif value == max_value:
            value_list.append(value)

    return value_list


def main():
    print(max_function(x=1, y=2, z=3))


main()
