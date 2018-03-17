'''
* Tuples: IMMUTABLE ordered sequence of items
* Similar to Lists, but elements are enclosed within parentheses & their size can NOT be changed (like lists)
* Expression separated by commas
'''
tuple1 = ('string 1', 12, 15.0, 'karol', 22)
tuple2 = 'string'
tuple3 = ()
tuple4 = ('rebeca',)
tuple5 = tuple()
# tuple6 = tuple(100, 200, 300)


print(tuple1)
print(tuple1[3])

# Error: impossible to update a tuple!
# tuple1[3] = 1000

print((1, 2, 3))    # >> (1, 2, 3)

print(1, 2, 3)      # >> 1, 2, 3