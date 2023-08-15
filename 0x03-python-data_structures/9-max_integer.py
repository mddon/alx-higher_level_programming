#!/usr/bin/python3


def max_integer(my_list=[]):

    if len(my_list) == 0:
        return (None)

    largest_int = my_list[0]
    for a in range(len(my_list)):
        if my_list[a] > largest_int:
           largest_int = my_list[a]

    return largest_int
