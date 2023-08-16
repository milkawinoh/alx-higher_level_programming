#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    def square(x):
        return x ** 2
    
    new_matrix = list(map(lambda row: list(map(square, row)), matrix))
    
    return new_matrix

