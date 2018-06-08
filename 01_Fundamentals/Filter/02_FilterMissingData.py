"""
    Simple Filter of a List: remove missing Data
"""


countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia", "", "Ecuador", "", "", "Peru"]

print(list(filter(None, countries)))
