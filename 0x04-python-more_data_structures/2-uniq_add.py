#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq_sum = 0
    for indexk in set(my_list):
        uniq_sum += indexk
    return uniq_sum
