#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x elements of a list."""
    count = 0
    try:
        for element in my_list[:x]:
            count = count + 1
            print("{:d}" .format(element), end="")
        print()

    except IndexError:
        for element in my_list[:x]:
            count = count + 1
            print("{:d}" .format(element), end="")
        print()
    return count
