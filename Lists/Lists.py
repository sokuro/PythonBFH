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
list6 = list((1, 2, 3))

print(list1)
print(list2)
print(list6)
