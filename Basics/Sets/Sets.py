"""
* Sets are unordered collections of unique items
* Sets MUST be hashable
* Sets: sets => mutable and not hashable
        frozenset => immutable and hashable
"""
set1 = {1, 2, 3}
set2 = {'one', 'two', 'three'}
set3 = {}                           # DICTIONARY!
set4 = set()                        # empty set

set5 = frozenset([1, 2, 3])         # frozenset from an iterable

# ERROR
# set6 = {{1, 2, 3}, {4}, {3.14}}     # set of sets is not allowed, set not hashable
# Solved with frozenset
set7 = {frozenset([1, 2, 3]), frozenset({4}), frozenset({3.14})}

print(set7)