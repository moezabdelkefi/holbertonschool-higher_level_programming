#!/usr/bin/python3

"""define a function that divides all elements of a matrix"""

"""
raises:
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    TypeError: Each row of the matrix must have the same size
    TypeError: div must be a number
    TypeError: division by zero

"""

def matrix_divided(matrix, div):
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(item, (int,float))for row in matrix for item in row):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_len = [len(row) for row in matrix]
    if not all(length == row_len[0] for length in row_len):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int ,float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row]for row in matrix]
