"""
    Area of a Circle with Radius 'r'
"""


# Definition to Calculate the Area of a Circle
def area(r):

    import math

    return math.pi * (r ** 2)


# List of Radii

radii = [2, 5, 7.1, 0.3, 10]


# 1) Direct Method using Loop
def direct_method():

    areas = []

    for r in radii:
        a = area(r)
        areas.append(a)

    return areas


# Use Map Function to Calculate Area for each Element
def map_method():

    return list(map(area, radii))


def main():

    print(direct_method())
    print(map_method())


main()
