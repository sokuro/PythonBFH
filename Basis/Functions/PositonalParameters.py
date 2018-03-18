"""
* A method can have variable number of positional parameters
* *args specifies extra positional parameters
* Convention is to call it *args
* Inside a function, args is a tuple that contains all provided positional arguments that are captured by *args
"""


def manual_sum(*args):
    summand = 0                     # shadows the ootb 'sum

    for x in args:
        summand += x
    return summand


s1 = manual_sum()
print(s1)                       # >> 0

s2 = manual_sum(1)
print(s2)                       # >> 1

s3 = manual_sum(1, 2)
print(s3)                       # >> 3


# adding a tuple
newTuple = [1, 2, 3, 4]

# ERROR => TypeError
# s4 = manual_sum(newTuple)     # can not add a list to an integer!

# Solution
s5 = manual_sum(*newTuple)
print(s5)                       # >> 10