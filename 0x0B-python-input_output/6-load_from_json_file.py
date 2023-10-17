#!/usr/bin/python3
"""Script that defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Load a Python object from a JSON formatted file.
    Args:
        filename (str): The name of the JSON file to load the object from.
    Returns:
        obj: The Python object loaded from the JSON file.
    Example:
        >>> loaded_data = load_from_json_file("data.json")
        >>> print(loaded_data)
        {'name': 'Prince', 'age': 40}
    """
    with open(filename) as f:
        return json.load(f)
