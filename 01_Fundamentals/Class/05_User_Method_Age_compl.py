"""
    Extending with Properties

    Extract the Properties

    Method: Age: Calculating the Age
"""


class User:

    def __init__(self, full_name, birthday):

        # attach Properties to the Object
        self.name = full_name
        self.birthday = str(birthday)   # convert to String

        # Extract first and last Names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[1]

    # get the Age of the User
    # calculating the Age
    def age(self):

        import datetime

        today = datetime.date.today()

        # convert to int
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])

        date_birth = datetime.date(yyyy, mm, dd)

        age_in_days = (today - date_birth).days
        age_in_years = age_in_days / 365

        return int(age_in_years)


def main():

    user = User('Karol Ugorcak', 19810415)

    print('Hello {} {}'.format(user.first_name, user.last_name) + '! You are {}'.format(user.age()) + ' years old.')


main()
