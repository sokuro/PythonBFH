"""
    calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
"""


# User Input
intInput = input('Input 3 Integers : ')

# Build a List from the Input
list = intInput.split(' ')

# convert to Integer
x = int(list[0])
y = int(list[1])
z = int(list[2])


def calculate_sum(x, y, z):

    sum = x + y + z

    if x == y == z:
        sum = sum * 3

    return sum


print(calculate_sum(x, y, z))
