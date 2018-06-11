"""
    Equality in Strings: ALWAYS '=='
"""

a = 'pub'
b = ''.join(['p', 'u', 'b'])

print('First Element: '"'{}'"''.format(a))      # >> First Element: 'pub'

print('Second Element: '"'{}'"''.format(b))     # >> Second Element: 'pub'

print(a == b)           # >> True

print(a is b)           # >> False (Java: equals())
