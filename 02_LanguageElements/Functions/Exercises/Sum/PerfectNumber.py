"""
    Function to check whether a number is perfect or not

    Perfect Number:
        > positive int
        > equal to the Sum of it's positive Divisors (incl. itself)

        > equal to the Half of the Sum of it's positive Divisors (incl. itself)
"""


def perfect_number(n):

    value_list = []
    sum = 0

    for num in range(1, n):
        if n % num == 0:
            sum += num
            value_list.append(sum)

    return value_list


def main():
    print(perfect_number(100))
    print(perfect_number(6))
    print(perfect_number(28))


main()
