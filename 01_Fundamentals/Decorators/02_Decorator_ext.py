"""
    Decorator: Function that takes another Function as Argument

    Extend the Wrapper with an extra Statement
"""


# Decorator
def decorator_function(original_function):

    def wrapper_function():

        # extra Statement
        print('wrapper executed this before {}'.format(original_function.__name__))

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

    decorated_display()         # >> wrapper executed this before display
                                # >> display Function


main()
