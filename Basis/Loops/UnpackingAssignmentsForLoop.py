"""
* The target can have multiple identifiers, like an unpacking assignment
"""


class UnpackingAssignmentsForLoop:

    birth_years = {'Rebeca': 1992, 'Daniel': 1994, 'Karol': 1981}

    for name, year in birth_years.items():
        print(f'{name} was born in {year}')