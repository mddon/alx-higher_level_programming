#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
    Return the integer sum of two numbers, a and b.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.
    Returns:
        Before the sum of a and b is performed, float arguments are type-casted to int.
    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
