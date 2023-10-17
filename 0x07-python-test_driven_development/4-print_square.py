#!/usr/bin/python3
"""This script defines a square-printing function."""


def print_square(size):
    """Print a square with the # character.
    Args:
        size (int): The size (height/width) of the square.
    Raises:
        TypeError: If size is not an integer or is a float.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for k in range(size):
        [print("#", end="") for i in range(size)]
        print("")
