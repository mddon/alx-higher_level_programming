#!/usr/bin/python3
"""Script that defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
