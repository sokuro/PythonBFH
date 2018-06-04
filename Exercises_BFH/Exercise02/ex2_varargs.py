"""
Exercises 2: Python Language Elements
BTI7541, Prof. Dr. René Müller

PART II: FUNCTIONS

Problem 4: Functions with variable number of arguments

In this assignment we use different functions with
variable arguments in Python. Please implement the functions
to make all test below pass.

a) Implement the function set_destination() that takes a variable
   number of positional and keyword arguments and prints
   the destination coordinates.

>>> point = (3, 8, 2)
>>> coordinates = {'x': 8, 'y': 33, 'z': -4}

>>> set_destination(*point)
Going to x=3, y=8, z=2

>>> set_destination(**coordinates)
Going to x=8, y=33, z=-4


b) Implement a function that computes and returns the product of all
   arguments, both, for positional and keyword arguments.

>>> values = {"a":3, "b":2, "c":4}
>>> some_values = {"c": 7, "b": 4}

>>> product(2, 7, 3)
42
>>> product(**values)
24
>>> product(1, **some_values)
28


c) Implement a function that computes and returns the total sum
   of all arguments, both, for positional and keyword arguments.

>>> amounts = {"u": 3, "v": 2, "w": 4}
>>> some_amounts = {"v": 7, "w": 4}
>>> total(1, 2, 3)
6
>>> total(**amounts)
9
>>> total(3, **some_amounts)
14


d) Implement a function that returns the largest even number
   of all arguments, both, for positional and keyword arguments.

>>> max_even(2, 3)
2
>>> max_even(2, 4)
4
>>> max_even(2, 3, 9, 11, 7, 8, 13, 21)
8


e) Implement a function that returns the value of the keyword
   argument with the longest name.

>>> country_populations = {
...     "Russia": 144,
...     "USA": 319,
...     "Philippines": 99,
...     "India": 1252,
... }

>>> val_for_longest_key(a=1)
1
>>> val_for_longest_key(a=2, aa=3)
3
>>> val_for_longest_key(foo=10, alpha=3, x=9)
3
>>> val_for_longest_key(**country_populations)
99


f) Implement a function that returns the name of the keyword
   argument with the largest value.

>>> key_for_biggest_value(a=1)
'a'
>>> key_for_biggest_value(a=2, aa=3)
'aa'
>>> key_for_biggest_value(foo=10, alpha=3, x=9)
'foo'
>>> key_for_biggest_value(**country_populations)
'India'

"""

# Write your code here:


def set_destination(*args, **kwargs):
    """Function takes a variable number of positional and keyword
       arguments and prints the destination coordinates."""
    # YOUR CODE HERE
    if args:
        print("Going to x={}, y={}, z={}".format(args[0], args[1], args[2]))

    if kwargs:
        print("Going to x={}, y={}, z={}".format(kwargs['x'], kwargs['y'], kwargs['z']))
    pass


def product(*args, **kwargs):
    """Function that returns the product of all arguments, both,
       for positional and keyword arguments."""
    # YOUR CODE HERE
    result = 1

    for x in args:
        result *= x

    for key, value in kwargs.items():
        result *= value

    return result


def total(*args, **kwargs):
    """Function that returns the total sum of all arguments, both,
       for positional and keyword arguments."""
    # YOUR CODE HERE
    sum = 0

    for x in args:
        sum += x

    for key, value in kwargs.items():
        sum += value

    return sum


def max_even(*args, **kwargs):
    """Function that returns the largest even number
       of all arguments, both, for positional and keyword arguments."""
    # YOUR CODE HERE
    evenNumber = None

    for x in args:
        if x % 2 == 0:
            evenNumber = x

    for key, value in kwargs.items():
        if value % 2 == 0:
            evenNumber = value

    return evenNumber


def val_for_longest_key(**kwargs):
    """Function that returns the value of the keyword argument with the
       longest name."""
    # YOUR CODE HERE
    keyList = []
    result = ""

    for key, value in kwargs.items():
        if key.__len__() > 0:
            keyList.append(key)

        longestKey = max(keyList, key=len)
        result = kwargs.get(longestKey)

    return result


def key_for_biggest_value(**kwargs):
    # YOUR CODE HERE
    valueList = []
    max_value = None

    for key, value in kwargs.items():
        if max_value is None or value > max_value:
            valueList = key
            max_value = value
        elif value == max_value:
            valueList.append(key)

    return valueList


if __name__ == '__main__':
    import doctest
    doctest.testmod()
