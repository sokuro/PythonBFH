"""
    Decorator: Function that takes another Function as Argument

    Extend the Wrapper with an extra Statement

    Use Annotation
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


# Annotaton for the Decorator Function
@decorator_function
def display():

    print('display Function')


def main():

    # display Function passed into the Decorator Function
    # Annotation used!
    display()


main()
