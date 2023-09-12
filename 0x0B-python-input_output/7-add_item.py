#!/usr/bin/python3
"""Add command-line arguments to a Python list and save them to a JSON file."""
import sys


if __name__ == "__main__":
    '''Necessary functions imported from external modules'''
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
    '''If the JSON file doesn't exist, initialize an empty list'''
        items = []
    '''Extend the 'items' list with command-line arguments'''
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
