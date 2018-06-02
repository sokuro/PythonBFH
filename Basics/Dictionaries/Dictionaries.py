"""
* fundamental data structure: every module, class, function, object
* Dictionary represents a mapping from a collection of key objects to a collection of value objects
* Every value stored in the dictionary is indexed by its key! Keys must be hashable-
"""
# key: string
example1 = {'x': 1, 'y': 2, 'z': 3}

print(example1)
print(example1['x'])                # >> 1

# key: int
example2 = {1: 1, 2: 2, 3: 3}
print(example2[2])                  # >> 2

# key: mixed
example3 = {1: 1, 'test1': 3, 3: 'test2'}
print(example3[3])                  # >> test2
