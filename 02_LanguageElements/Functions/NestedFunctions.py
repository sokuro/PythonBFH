"""
    Functions can contain Functions
"""


def outer_function(x):          # x = 7
    y = x + 1                   # y = 8

    # nested Function
    def inner_function(z):      # z = y = 8
        return x + y + z        # 7 + 8 + 8

    return inner_function(y)


def main():
    r = outer_function(7)
    print(r)                    # >> 23


main()
