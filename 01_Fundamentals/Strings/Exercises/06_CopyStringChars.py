"""
    get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2
"""


def copy_chars(str, times):

    str_length = 2

    if len(str) <= str_length:
        str_length = len(str)

    substr = str[:str_length]

    result = ''

    for i in range(times):
        result += substr

    print(result)


copy_chars('B', 5)
copy_chars('Bl', 5)
copy_chars('Blablabla', 5)

