# Escape characters are not interpreted in raw string
import re
pattern = re.compile(r'\d+\.\d*')           # r : raw string
match = re.fullmatch(pattern, '3.14')
print(match)


pattern2 = re.compile('\\d+\\.\\d*')
match2 = re.fullmatch(pattern2, '3.14')
print(match2)