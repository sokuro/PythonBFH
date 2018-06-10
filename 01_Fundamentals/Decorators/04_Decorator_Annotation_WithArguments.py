"""
    Decorator: Function that takes another Function as Argument

    Extend the Wrapper with an extra Statement

    Use Annotation for both Functions without Error: *args, **kwargs

    Extend with Arguments
"""


# Decorator
def decorator_function(original_function):

    # use *args, **kwargs to prevent Error, that both Functions are
    # passed into the wrapper Function
    def wrapper_function(*args, **kwargs):

        # extra Statement
        print('wrapper executed this before {}'.format(original_function.__name__))

        # pass the Argument directly into the inner Function
        # execute the Function
        # use *args, **kwargs
        original_function(*args, **kwargs)

    # by removing the () the Function is waiting to be executed
    return wrapper_function


# Annotaton for the Decorator Function
@decorator_function
def display():

    print('display Function')


# Display Info
@decorator_function
def display_info(name, age):

    print('display_info ran with arguments ({}, {})'.format(name, age))


def main():

    # display Function passed into the Decorator Function
    # Annotation used!
    display()

    # display with extended Arguments
    display_info('Karol', 37)


main()
