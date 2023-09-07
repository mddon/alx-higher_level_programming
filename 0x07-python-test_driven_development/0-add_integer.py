#!/usr/bin/python3
""" This script defines an integer addition function."""

def add_integer(a, b=98):
    """
    Return the integer sum of  two numbers, a and b.
    Before a and b are summed, float arguments are type-casted to int.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
