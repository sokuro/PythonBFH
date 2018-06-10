"""
    Testing nested Functions
"""


def outer():

    x = 'outer x'

    # inner Function
    def inner():

        x = 'inner x'

        print(x)                # inner x

    # call the inner Function
    inner()

    print(x)                    # outer x


def main():

    outer()


main()
