"""
    Functions are Objects that can have Attributes too
"""


def counter():
    counter.count += 1
    return counter.count


counter.count = 0


def main():
    counter()
    print(counter())        # >> 2


main()
