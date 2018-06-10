"""
    Decorators

    Closure
"""

def outer_function():

    message = 'Hi'

    def inner_function():

        print(message)

    # by removing the () the Function is waiting to be executed
    return inner_function


def main():

    # assign to a Variable
    my_func = outer_function()

    # using Closure: remembers the 'message' Variable of the outer Function
    my_func()
    my_func()
    my_func()


main()
