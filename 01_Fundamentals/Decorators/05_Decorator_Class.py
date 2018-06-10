"""
    Decorator: Class
"""


# Decorator
def decorator_function(original_function):

    def wrapper_function(*args, **kwargs):

        print('wrapper executed this before {}'.format(original_function.__name__))

        return original_function(*args, **kwargs)

    return wrapper_function


# Decorator Class
class decorator_class(object):

    def __init__(self, original_function):

        # tied the Original Function to the Instance of the Class
        self.original_function = original_function

    def __call__(self, *args, **kwargs):

        # using the Functionality of the old Wrapper Function
        print('wrapper executed this before {}'.format(self.original_function.__name__))

        return self.original_function(*args, **kwargs)


# Annotation for the Decorator Class
@decorator_class
def display():

    print('display Function')


# Display Info
@decorator_class
def display_info(name, age):

    print('display_info ran with arguments ({}, {})'.format(name, age))


def main():

    # display Function passed into the Decorator Function
    # Annotation used!
    display()

    # display with extended Arguments
    display_info('Karol', 37)


main()
