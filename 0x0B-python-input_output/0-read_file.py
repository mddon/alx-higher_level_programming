#!/usr/bin/python3
"""Script that defines a text file-reading function."""


def read_file(filename=""):
    """Read and print the contents of a UTF-8 encoded text file.
    Args:
        filename (str, optional): The path to the text file to be read.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
