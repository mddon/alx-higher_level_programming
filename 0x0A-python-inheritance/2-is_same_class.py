#!/usr/bin/python3
"""The script defines a function to check if an object is an instance of a specific class."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.
    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
