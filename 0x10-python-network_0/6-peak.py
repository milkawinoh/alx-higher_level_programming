def find_peak(list_of_integers):
    """
    Find a peak in an unsorted list of integers.

    Args:
        list_of_integers (list): Unsorted list of integers.

    Returns:
        int | None: Peak element.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        # Compare mid with its neighbors
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
