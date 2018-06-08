"""
    Using nonlocal to bind the Variable
"""


def outer_function(x):
    y = x + 1

    # nested function
    def inner_function(z):
        nonlocal y          # bind Variable from the outer Scope
        y += 1
        return x + y + z

    return inner_function(y)


def main():
    r = outer_function(7)
    print(r)


main()