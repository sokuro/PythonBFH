"""
* First, a tuple is created
* Unpacking assignment decomposes tuple and stores items in reverse order
* NO tuple OBJECT is generated!
"""
a = 5
print('The variable a before swapping has the value: ', a)

b = 10
print('The variable b before swapping has the value: ', b, '\n')

# swap the variables
a, b = b, a

print('The variable a after swapping has the value: ', a)

print('The variable b after swapping has the value: ', b)