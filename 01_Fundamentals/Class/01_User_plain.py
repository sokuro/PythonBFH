"""
    Defining a Class NEEDS ALWAYS 1 Line of a Code!

    Class without Constructor
"""


class User:
    pass


def main():

    user = User()

    # adding Properties
    user.first_name = 'Karol'
    user.last_name = 'Ugorcak'

    print('Hello {} {}'.format(user.first_name, user.last_name) + '!')


main()
