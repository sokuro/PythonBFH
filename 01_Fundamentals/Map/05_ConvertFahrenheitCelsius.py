"""
    Map Data: convert the Data Values in °C in the List to °F

    Formula °F = 9/5 * °C + 32
"""


l = [("Berlin", 29),
     ("Cairo", 36),
     ("Buenos Aires", 19),
     ("Los Angeles", 26),
     ("Tokyo", 27),
     ("New York", 28),
     ("London", 22),
     ("Beijing", 32)]


def convert_c_to_f():

    return list(map(lambda data: (data[0], (9/5) * data[1] + 32), l))


def main():

    print(convert_c_to_f())


main()
