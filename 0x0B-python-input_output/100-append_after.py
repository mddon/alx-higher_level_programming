#!/usr/bin/python3
"""This script defines a text file modification function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as rd:
        for line in rd:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as wr:
        wr.write(text)
