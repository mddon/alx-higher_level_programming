#!/usr/bin/python3
"""Script that defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.
    Returns:
        bool: True if obj is an instance or inherited instance of a_class, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
