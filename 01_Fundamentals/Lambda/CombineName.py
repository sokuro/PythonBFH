"""
    Combine Name with Lambda

    Lambda as anonymous Function
"""


# str.strip(): Copy of str with Whitespace trimmed
# str.title(): Start Letter capitalized
full_name = lambda first_name, last_name: first_name.strip().title() + " " + last_name.strip().title()


""" acc. PEP8 it is not good to assign a lambda Expression, but using def """
def generate_full_name(first_name, last_name):

    return first_name.strip().title() + " " + last_name.strip().title()


def main():

    print(full_name("Karol", "Ugorcak"))
    print(generate_full_name("Karol", "Ugorcak"))


main()
