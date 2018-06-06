def add(*, x, y, z):                # named parameters
    return x + y + z


result1 = add(x=1, y=2, z=3)


# TypeError! add() takes 0 positional Arguments!
# result2 = add(1, 2, 3)


print(result1)
# print(result2)
