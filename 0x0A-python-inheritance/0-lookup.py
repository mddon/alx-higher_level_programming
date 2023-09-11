#!/usr/bin/python3
"""Script that defines an object attribute lookup function."""

def lookup(obj):
    """
    Return a list of attributes and methods available for an object.
    Args:
        obj (object): The object to inspect.
    Returns:
        list: A list of available attributes and methods of the object.
    """
    return dir(obj)
