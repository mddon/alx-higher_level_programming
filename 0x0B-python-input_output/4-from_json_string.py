#!/usr/bin/python3
"""This script defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Converts a JSON string to its corresponding Python object.
    Args:
        my_str (str): The JSON string to be converted.
    Returns:
        obj: The Python object represented by the JSON string.
    Example:
        >>> from_json_string('{"name": "Peace", "age": 27}')
        {'name': 'Peace', 'age': 27}
    """
    return json.loads(my_str)
