"""
    Input: int(n) or string
    Output: n+nn+nnn
"""


intInput = int(input('Input an integer: '))

n1 = int('%s' % intInput)
n2 = int('%s%s' % (intInput, intInput))
n3 = int('%s%s%s' % (intInput, intInput, intInput))


print(n1+n2+n3)
