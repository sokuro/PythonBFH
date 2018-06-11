"""
    count repeated characters in a string

    using Collections
"""
import collections

str_input = input('Enter a String: ')

counter = collections.defaultdict(int)


for char in str_input:

    counter[char] += 1


# Sorting the Characters and Formatting them
for char in sorted(counter, key=counter.get, reverse=True):

    if counter[char] > 1:

        # %s : string
        # %d : decimal
        print('%s : %d' % (char, counter[char]))
