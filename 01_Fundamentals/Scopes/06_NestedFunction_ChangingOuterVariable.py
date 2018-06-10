"""
    Testing nested Functions: Enclosing Scope

    Changing the 'outer x' from inside of the inner Function

    Preventing to use GLOBAL statement!!! Changes are made ONLY inside
    of the Outer Function!
"""


def outer():

    x = 'outer x'

    # inner Function
    def inner():

        # using nonlocal one changes the 'outer x' from inside of inner()
        nonlocal x

        x = 'inner x'

        print(x)                # inner x

    # call the inner Function
    inner()

    print(x)                    # inner x


def main():

    outer()


main()
