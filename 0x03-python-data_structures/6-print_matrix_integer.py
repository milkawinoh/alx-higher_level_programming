#!/usr/bin/python3
"""
a function that prints a matrix of integers.
"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for n in row:
            print("{:d}".format(n), end=" ")
        print()
