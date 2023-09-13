#!/usr/bin/python3
"""This script defines a text file modification function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file.
    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for within each line.
        new_string (str): The string to insert after each line containing the search string.
    """
    modified_content = ""
    with open(filename) as file_reader:
        for line in file_reader:
            modified_content += line
            if search_string in line:
                modified_content += new_string
    with open(filename, "w") as file_writer:
        file_writer.write(modified_content)
