#!/usr/bin/python3

def search_replace(my_list, search, replace):

    updated_list = my_list[:]

    for k in range(len(updated_list)):
        if updated_list[k] == search:
            updated_list[k] = replace

    return updated_list
