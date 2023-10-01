#!/usr/bin/python3
"""Module for matrix_divided metod."""


def matrix_divided(matrix, div):
    """Divide all elements of the matrix by div.
    Args:
        matrix: list of lists contains float or int.
        div: number to divide matrix by.
    Return:
        list: list of lists of a divided matrix.
    Raises:
        TypeError: If matrix is not list of lists of integers or floats.
        TypeError: If Each row of the matrix is not the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in row:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(j / div, 2) for j in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
