"""
* If both the *args & **kwargs are present, **kwargs MUST come after!
"""


def temp(*args, **kwargs):

    for x in args:
        print(x)

    for k, v in kwargs.items():
        print(f'{k} = {v}')


temp()

temp(a=42)                  # >> a = 42

temp(1, a=10, b=11)         # >> 1; a = 10; b = 11


# adding a new tuple
newTuple = (1, 2, 3)
temp(newTuple)              # >> (1, 2, 3)
temp(*newTuple)             # >> 1 2 3


# adding a new object
newObject = {'x': 20, 'y': 30}
temp(1, newObject)          # >> 1; {'x': 20, 'y': 30}
temp(1, *newObject)         # >> 1; x; y

# combining *args & **kwargs
temp(*newTuple, **newObject)    # >> 1; 2; 3; x = 20; y = 30