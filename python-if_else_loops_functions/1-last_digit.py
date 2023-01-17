#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(repr(number)[-1])
if last_digit > 5:
    print(f"and is greater than5")
elif last_digit == 0:
	print(f"and is 0")
elif last_digit < 6:
	print(f"and is less than 6 and not 0")
	