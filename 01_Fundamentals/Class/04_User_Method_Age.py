"""
    Extending with Properties

    Extract the Properties

    Method: Age
"""


class User:

    def __init__(self, full_name, birthday):

        # attach Properties to the Object
        self.name = full_name
        self.birthday = birthday

        # Extract first and last Names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[1]
        self.birth_year = int(str(birthday)[0:4])

    # get the Age of the User
    # using the datetime method today()
    def age(self):

        import datetime

        today = datetime.date.today().year

        return today - self.birth_year


def main():

    user = User('Karol Ugorcak', 19810415)

    print('Hello {} {}'.format(user.first_name, user.last_name) + '! You were born in {}'.format(user.birth_year) + '.')

    print(user.age())


main()
