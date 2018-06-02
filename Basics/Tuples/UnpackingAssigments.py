"""
* An iterable can be unpacked into individual items
* Formatted f-string literal
"""

temp = ('Karol', 1981, 'SK')

name, year, nationality = temp      # unpacking assignment

print(f'{name} was born in {year} and is from {nationality}.')