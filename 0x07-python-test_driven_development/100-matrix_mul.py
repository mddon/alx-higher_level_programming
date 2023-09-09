#!/usr/bin/python3
'''Python script that contain the functions for matrix multiplication'''

def get_matrix_sizes(matrix, name):
    # Helper function to check if a matrix is valid
    if not isinstance(matrix, list):
        raise TypeError('{} must be a list'.format(name))
    if not matrix:
        raise ValueError('{} can\'t be empty'.format(name))
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError('{} must be a list of lists'.format(name))
    if any(not all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError('{} should contain only integers or floats'.format(name))
    if len(set(len(row) for row in matrix)) != 1:
        raise ValueError('Each row of {} must be of the same size'.format(name))

def matrix_mul(m_a, m_b):
    # Get the sizes of matrices and validate
    get_matrix_sizes(m_a, 'm_a')
    get_matrix_sizes(m_b, 'm_b')

    # Calculate the sizes of the matrices
    size_a = [len(m_a), len(m_a[0])]
    size_b = [len(m_b), len(m_b[0])]

    # Check if matrices can be multiplied
    if size_a[1] != size_b[0]:
        raise ValueError('m_a and m_b can\'t be multiplied')

    # Initialize the result matrix
    result = [[0 for _ in range(size_b[1])] for _ in range(size_a[0])]

    # Perform matrix multiplication
    for i in range(size_a[0]):
        for j in range(size_b[1]):
            for k in range(size_a[1]):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
