#!/usr/bin/python3
"""Script that defines an object attribute lookup function."""


def lookup(obj):
    """Returns a list of available attributes and methods of the object."""
    return dir(obj)
