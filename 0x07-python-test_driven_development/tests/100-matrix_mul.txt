    Multiply two matrices.

    This function takes two matrices, m_a and m_b, and multiplies them together.

    Args:
        m_a (list of list of int or float): The first matrix.
        m_b (list of list of int or float): The second matrix.

    Returns:
        list of list of int or float: The result of multiplying m_a and m_b.

    Raises:
        TypeError: If the input matrices are not valid (not lists of lists).
        ValueError: If the input matrices are empty or have incompatible dimensions.

    Examples:
        # Import the required function
        >>> from importlib import import_module
        >>> matrix_mul = import_module('100-matrix_mul').matrix_mul

        # Valid arguments
        >>> matrix_mul([[2, 3]], [[4], [5]])
        [[23]]
        >>> matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[19, 22], [43, 50]]
        >>> matrix_mul([[2, 4, 6], [8, 10, 12]], [[1, 3], [5, 7], [9, 11]])
        [[58, 70], [124, 154]]

        # Invalid arguments
        >>> try:
        ...     matrix_mul(42, [[4, 6]])
        ... except TypeError as ex:
        ...     print(ex.args[0])
        'm_a must be a list'
        >>> try:
        ...     matrix_mul([[4, 6]], 42)
        ... except TypeError as ex:
        ...     print(ex.args[0])
        'm_b must be a list'
        >>> try:
        ...     matrix_mul(['[4, 6]'], 42)
        ... except TypeError as ex:
        ...     print(ex.args[0])
        'm_a must be a list'
        >>> try:
        ...     matrix_mul([(4, 6)], [42])
        ... except TypeError as ex:
        ...     print(ex.args[0])
        'm_a must be a list of lists'
        >>> try:
        ...     matrix_mul([], [[42]])
        ... except ValueError as ex:
        ...     print(ex.args[0])
        "m_a can't be empty"
        >>> try:
        ...     matrix_mul([['2', '3']], [[]])
        ... except ValueError as ex:
        ...     print(ex.args[0])
        "m_b can't be empty"
        >>> try:
        ...     matrix_mul([[]], [[42]])
        ... except ValueError as ex:
        ...     print(ex.args[0])
        "m_a can't be empty"
        >>> try:
        ...     matrix_mul([[], []], [[42]])
        ... except ValueError as ex:
        ...     print(ex.args[0])
        "m_a can't be empty"
        >>> try:
        ...     matrix_mul([[1, 6], [3, 3]], [[]])
        ... except ValueError as ex:
        ...     print(ex.args[0])
        "m_b can't be empty"
        >>> try:
        ...     matrix_mul([[4, '6', 8]], [[12]])
        ... except TypeError as ex:
        ...     print(ex.args[0])
        'm_a should contain only integers or floats'
        >>> try:
        ...     matrix_mul([[4, '6', 8]], [['12']])
        ... except TypeError as ex:
        ...     print(ex.args[0])
        'm_a should contain only integers or floats'
        >>> try:
        ...     matrix_mul([[4, 6, 8], []], [[(12, )]])
        ... except TypeError as ex:
        ...     print(ex.args[0])
        'm_b should contain only integers or floats'
        >>> try:
        ...     matrix_mul([[4, 6, 8], []], [[12, 3]])
        ... except TypeError as ex:
        ...     print(ex.args[0])
        'each row of m_a must be of the same size'
        >>> try:
        ...     matrix_mul([[4, 6, 8], [1, 2, 3]], [[12, 3], []])
        ... except TypeError as ex:
        ...     print(ex.args[0])
        'each row of m_b must be of the same size'
        >>> try:
        ...     matrix_mul([[4, 6, 8], [1]], [[12, 3]])
        ... except TypeError as ex:
        ...     print(ex.args[0])
        'each row of m_a must be of the same size'
        >>> try:
        ...     matrix_mul([[4, 6, 8], [4, 4, 4]], [[12, 3], [7]])
        ... except TypeError as ex:
        ...     print(ex.args[0])
        'each row of m_b must be of the same size'
        >>> try:
        ...     matrix_mul([[4, 6, 8], [1, 3, 7]], [[12, 3]])
        ... except ValueError as ex:
        ...     print(ex.args[0])
        "m_a and m_b can't be multiplied"
        >>> try:
        ...     matrix_mul([[1, 2], [3, 4]], [[5, 6], [7.5, 8], [9, 10]])
        ... except ValueError as ex:
        ...     print(ex.args[0])
        "m_a and m_b can't be multiplied"
