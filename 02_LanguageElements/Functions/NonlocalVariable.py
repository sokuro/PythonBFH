"""
    Using nonlocal to bind the Variable
"""


def outer_function(x):      # x = 7
    y = x + 1               # y = 8

    # nested function
    def inner_function(z):  # z = y = 8
        nonlocal y          # bind Variable from the outer Scope
        y += 1              # y + 1 = 8 + 1 = 9
        return x + y + z    # 7 + 9 + 8

    return inner_function(y)


def main():
    r = outer_function(7)
    print(r)                # >> 24


main()
