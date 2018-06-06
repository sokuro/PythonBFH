"""
    Parameters with default Values
    Default Values can be mutable
"""


def f(x, y=None):
    if y is None:
        y = []

    y.append(x)

    return y


print(f(1))

print(f(2))
