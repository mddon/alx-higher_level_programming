#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    return [list(map(lambda k_element: k_element * k_element, row)) for row in matrix]
