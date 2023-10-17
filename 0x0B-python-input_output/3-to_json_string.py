#!/usr/bin/python3
"""This script defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Converts a Python object to its JSON representation.
    Args:
        my_obj: The Python object to be converted to JSON.
    Returns:
        str: A JSON representation of the input object.
    Example:
        >>> to_json_string({"name": "Max", "age": 20})
        '{"name": "Max", "age": 20}'
    """
    return json.dumps(my_obj)
