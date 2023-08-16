#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(r, a_dictionary[r])) for r in sorted(a_dictionary)]
