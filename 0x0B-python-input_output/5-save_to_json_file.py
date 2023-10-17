#!/usr/bin/python3
"""Script that defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Save a Python object to a JSON formatted file.
    Args:
        my_obj (obj): The Python object to be saved.
        filename (str): The name of the JSON file to save the object to.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
