#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    # Create the initial row of the triangle
    row = [1]
    result = [row]

    # Build up the remaining rows of the triangle
    for i in range(1, n):
        # Generate the next row of the triangle
        row = [1] + [row[j] + row[j+1] for j in range(len(row)-1)] + [1]
        result.append(row)

    return result
