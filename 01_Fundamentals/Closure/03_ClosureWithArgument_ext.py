"""
    Closure

    Pass the Argument directly into the inner Function
"""


# extend with Variable
def outer_function(msg):

    def inner_function():

        # pass the Argument directly into the inner Function
        print(msg)

    # by removing the () the Function is waiting to be executed
    return inner_function


def main():

    # assign to a Variable
    # unique message Variable
    hi_func = outer_function("Hi")
    bye_func = outer_function("Bye")

    # using Closure
    hi_func()       # >> Hi
    bye_func()      # >> Bye


main()
