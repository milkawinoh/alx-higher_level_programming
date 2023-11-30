ef find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integer using binary search tree approach.

    Args:
    - list_of_integers: A list of unsorted integers.

    Returns:
    - A peak element.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]
