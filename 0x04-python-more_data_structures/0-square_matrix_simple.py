#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return ([list(map(lambda xElement: xElement * xElement, row)) for row in matrix])
