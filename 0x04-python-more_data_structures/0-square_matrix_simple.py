#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return ([list(map(lambda k: k * k, row)) for row in matrix])
