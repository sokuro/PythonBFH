"""
* Lists are MUTABLE ordered sequence of items
* Lists may be of different type
* [] brackets
* Expressions separated by a comma
"""
list1 = [1, 2.14, 'test']
list2 = [42]
list3 = []          # empty list
list4 = list()      # empty list

# ERROR
# list5 = list(1, 2, 3)
# Solving
list6 = list((1, 2, 3)) # List out of the Tuple

print(list1)    # >> [1, 2.14, 'test']
print(list2)    # >> [42]
print(list3)    # >> []
print(list4)    # >> []
print(list6)    # >> [1, 2, 3]
