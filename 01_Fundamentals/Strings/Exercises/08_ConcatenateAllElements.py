"""
    concatenate all elements in a list into a string and return it
"""


def concatenate_Elements(list):

    result = ''

    for element in list:
        result += str(element)

    print(result)


concatenate_Elements([1, 'true', 'Karol'])
