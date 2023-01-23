#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    new = '\n'.join([''.join(['{:4}'.format(i)
                    for i in row]) for row in matrix])
    print(new)
