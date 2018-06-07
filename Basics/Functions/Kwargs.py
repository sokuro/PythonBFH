"""
* **kwargs can be used to specify a variable number of keyword parameters
* Inside the function kwargs is a dictionary containing the supplied parameter name as key and their value as dictionary value
"""


def temp(**kwargs):

    for k, v in kwargs.items():
        print(f'{k} = {v}')     # k: key, v: value


temp()

print('\n')

temp(x=1)                       # >> x = 1

print('\n')

temp(x=1, y=3)                  # >> x = 1, y = 3

print('\n')

# defining a new dictionary
d = {'z': 10, 'w': 11}

temp(x=d)                       # >> x = {'z': 10, 'w': 11}

# ERROR => TypeError
# temp(d)                       # >> temp() takes 0 positional arguments, but was given 1

# Solution
temp(**d)                       # >> z = 10, w = 11