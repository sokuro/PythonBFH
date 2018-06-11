"""
    Extending with Properties
"""


class User:

    def __init__(self, full_name, birthday):

        # attach Properties to the Object
        self.name = full_name
        self.birthday = birthday


def main():

    user = User('Karol Ugorcak', 19810415)

    # print the birth_year of the User
    # 1) convert the int into str
    # 2) substring
    # 3) convert back into int
    birth_year = int(str(user.birthday)[:4])
    print('Hello {}'.format(user.name) + '! Your were born in {}'.format(birth_year) + '.')

    # in one Line
    print('Hello {}'.format(user.name) + '! Your were born in {}'.format(int(str(user.birthday)[:4])) + '.')


main()
