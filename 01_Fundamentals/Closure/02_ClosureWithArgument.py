"""
    Closure

    Extend the Function with a Variable
"""


# extend with Variable
def outer_function(msg):

    # assign to the passed Variable
    message = msg

    def inner_function():

        print(message)

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
