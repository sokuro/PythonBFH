"""
    map(f, x) returns an Iterator that applies the Function f on every Item
"""


l = [1, 2, 3, 4]


# With Loop
def map_loop(l):

    temp_list = []

    for num in l:
        temp_list.append(num + 1)

    return temp_list


# map and function
def inc(x):
    return x + 1


def map_function(l):
    return list(map(inc, l))


# map with Lambda (Redundancy! => Lambda is anonym)
def map_lambda(l):
    return list(map(lambda x: x + 1, l))


# elegant (but no PEP 8)
r = list(map(lambda x: x + 1, l))


def main():
    print(map_loop(l))
    print(map_function(l))
    print(map_lambda(l))
    print(r)


main()
