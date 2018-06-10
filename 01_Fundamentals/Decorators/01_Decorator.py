"""
    Decorator: Function that takes another Function as Argument
"""


# Decorator
def decorator_function(original_function):

    def wrapper_function():

        # pass the Argument directly into the inner Function
        # execute the Function
        return original_function()

    # by removing the () the Function is waiting to be executed
    return wrapper_function


# Display the Decorator
def display():

    print('display Function')


def main():

    # display Function passed into the Decorator Function
    decorated_display = decorator_function(display)

    decorated_display()


main()
