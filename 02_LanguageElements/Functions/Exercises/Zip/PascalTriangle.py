"""
    Function to print the Pascal Triangle

    use: zip
        > zip('ABCD', 'xy') --> Ax By
"""


def pascal_triangle(n):

    temp_row = [1]
    y = [0]

    for x in range(max(n, 0)):

        print(temp_row)         # build row

        temp_row = [l+r for l, r in zip(temp_row + y, y + temp_row)]

    return n >= 1


def main():
    # pascal_triangle(1)
    # pascal_triangle(2)
    pascal_triangle(3)


main()
