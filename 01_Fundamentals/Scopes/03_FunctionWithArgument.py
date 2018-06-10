"""
    foo(z)

    with a Parameter the Values are passed into the Function
"""


def foo(z):

    x = 'local x'

    print(z)        # >> z overwrites local x


def main():

    foo('local z')  # >> local z

    # print(z)        # ERROR: undefined!


main()
