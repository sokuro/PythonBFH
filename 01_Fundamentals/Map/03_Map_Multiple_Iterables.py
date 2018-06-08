"""
    Generated Iterator terminates when the End of the Shortest Input Iterator runs out of Elements
"""


l = [1, 2, 3, 4, 5, 6]
t = (True, False, False, True)
s = 'Hello World'

result = list(map(lambda n, b, c: '{}-{}-{}'.format(n, b, c), l, t, s))

print(result)
