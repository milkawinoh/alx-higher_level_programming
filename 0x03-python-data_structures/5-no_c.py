#!/usr/bin/python3
"""
a function that removes all characters c and C from a string.
"""


def no_c(my_string):
    new_string = ""
    for letter in my_string:
        if letter == 'c' or letter == 'C':
            continue
        else:
            new_string += letter
    return new_string
