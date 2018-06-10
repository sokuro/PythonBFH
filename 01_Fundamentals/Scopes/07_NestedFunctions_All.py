"""
    Testing nested Functions: Enclosing Scope
"""


x = 'global x'


def outer():

    x = 'outer x'

    # inner Function
    def inner():

        x = 'inner x'

        print(x)                # inner x

    # call the inner Function
    inner()

    print(x)                    # inner x


def main():

    outer()

    print(x)                    # global


main()
