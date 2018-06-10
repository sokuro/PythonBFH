"""
    sort(...)
        L.sort(key=None, reverse=False)
"""


# List of Names
names = ["Karol", "Rebeca", "Daniel", "Michael", "Patrik", "Richard"]


# sort alphabetically
names.sort()

print(names)

# sort reversed
names.sort(reverse=True)

print(names)


# Tuple of Names
names_tuple = ("Karol", "Rebeca", "Daniel", "Michael", "Patrik", "Richard")


# names_tuple.sort()      # ERROR: Tuples are not mutable!

