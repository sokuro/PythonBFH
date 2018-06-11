"""
    count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
"""


l = ['abc', 'xyz', 'aba', '1221']

counter = 0

for x in l:

    if len(x) > 1 and x[0] == x[-1]:

        counter += 1

print(counter)
