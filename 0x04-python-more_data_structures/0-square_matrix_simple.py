#!/bin/usr/python3
def square_matrix_simple(matrix=[]):
    new_list = matrix.copy()
    for i in range(len(matrix)):
        new_list[i] = [x**2 for x in matrix[i]]
    return (new_list)
