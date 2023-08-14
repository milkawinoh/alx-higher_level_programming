#!/usr/bin/python3

"""
a function that prints all integers of a list, in reverse order.
"""


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for list in my_list:
        print("{}" .format(list))
