#!/usr/bin/python3
from sys import argv

result = 0

for arg in argv[1:]:
    result += int(arg)

# Print the result of the addition
print(result)
