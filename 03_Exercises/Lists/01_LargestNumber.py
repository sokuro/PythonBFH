"""
    get the largest number from a list
"""


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

max = l[0]

for num in l:

    if num > max:

        max = num

print(max)
