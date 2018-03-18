def add(*, x, y, z):                # named parameters
    return x + y + z


result = add(x=1, y=2, z=3)

print(result)