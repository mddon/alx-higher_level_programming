#!/usr/bin/python3
"""Script that defines a function for adding attributes to objects."""


def add_attribute(obj, att, value):
    """Add new attribute to an object if possible.
    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
