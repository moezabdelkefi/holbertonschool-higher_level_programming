#!/usr/bin/python3

"""define a function that divides all elements of a matrix"""

"""
raises:
    TypeError: size must be an integer
    ValueError: size must be >= 0
    TypeError: size must be an integer

"""

def print_square(size):
    """ 
print a square with the character # 
    """

    if size == int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(1, size * size + 1):
        if i % size == 0:
            print("#")
        else:
            print("#", end='')

