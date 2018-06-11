"""
    1 Row Expression that returns a Number from [1:650] that is divided by 5 and 13 but NOT by 39
"""


def divide_number():
    for num in range(1, 651):
        if num % 5 == 0 and num % 13 == 0 and num % 39 != 0:
            print([num])


divide_number()

# in one Line:
print([num for num in range(1, 651) if num % 5 == 0 and num % 13 == 0 and num % 39 != 0])


"""
    filter creates a List of Elements for which the Function returns #true
"""
print(list(filter(lambda x: x % 5 == 0 and x % 13 == 0 and x % 39 != 0, range(1, 651))))
# >> [65, 130 ...]

"""
    map applies function to all items
"""
print(list(map(lambda x: x % 5 == 0 and x % 13 == 0 and x % 39 != 0, range(1, 651))))
# >> [False, False ...]

