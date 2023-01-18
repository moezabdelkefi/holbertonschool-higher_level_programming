#!/usr/bin/python3
smallest_combination = (0, 1)
for i in range(10):
    for j in range(i+1, 10):
        if (i, j) < smallest_combination:
            smallest_combination = (i, j)
print("{}{}".format(smallest_combination[0], smallest_combination[1]))
