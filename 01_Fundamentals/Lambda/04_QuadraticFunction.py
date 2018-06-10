"""
    Quadratic Function f(x) = ax^2 + bx + c)
"""


def build_quadratic_function(a, b, c):

    return lambda x: a*x**2 + b*x + c


def main():

    f = build_quadratic_function(1, 2, 3)

    # elegant way
    g = build_quadratic_function(1, 2, 3)(1)

    print(f(1))

    print(g())      # ERROR: 'int' Object is not callable!

    print(g)


main()
