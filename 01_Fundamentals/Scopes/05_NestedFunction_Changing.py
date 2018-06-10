"""
    Testing nested Functions: Enclosing Scope

    Commenting out the 'inner x'
"""


def outer():

    x = 'outer x'

    # inner Function
    def inner():

        # if 'inner x' is commented out, the 'outer x' is used
        # x = 'inner x'

        print(x)                # outer x

    # call the inner Function
    inner()

    print(x)                    # outer x


def main():

    outer()


main()
