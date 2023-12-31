#!/usr/bin/python3
"""Scipt that defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Check if an object is an inherited instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        bool: True if obj is an inherited instance of a_class.
        False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
