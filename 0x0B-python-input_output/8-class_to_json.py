#!/usr/bin/python3
"""Script that defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Returns the dictionary description of a simple data structure."""
    return obj.__dict__
