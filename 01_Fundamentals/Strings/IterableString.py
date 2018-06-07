"""
* Strings are immutable
* Because of this it is more efficient to accumulate the parts of the string in a list, which is mutable & then join the parts when the full string is necessary
"""
import timeit
"""
Calculate the program run time
"""

# 1) Create a concatenated string from 0 -> 9
start1 = timeit.default_timer()

nums = ""
for n in range(10):
    nums += str(n)                  # slow & inefficient
print(nums)
stop1 = timeit.default_timer()

print((stop1 - start1), 's')        # >> 3.2e-05 s

# 2) Create a concatenated string from 0 -> 9
start2 = timeit.default_timer()

nums = []
for n in range(10):
    nums.append(str(n))
print("".join(nums))
stop2 = timeit.default_timer()

print((stop2 - start2), "s")        # >> 1.33e-05 s

# 3) Create a concatenated string from 0 -> 9
start3 = timeit.default_timer()

nums = [str(n) for n in range(10)]
print("".join(nums))
stop3 = timeit.default_timer()

print((stop3 - start3), 's')        # >> 1.11e-05 s

# 4) Create a concatenated string from 0 -> 9
start4 = timeit.default_timer()

nums = map(str, range(10))
print("".join(nums))

stop4 = timeit.default_timer()
print((stop4 - start4), 's')        # >> 1.05e-05 s