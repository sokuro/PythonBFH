"""
    Local Variable inside the foo()

    Global Variable outside the foo()
"""

x = 'global x'


def foo():

    x = 'local x'

    print(x)  # >> local x


def main():
    foo()

    print(x)  # >> global x


main()
