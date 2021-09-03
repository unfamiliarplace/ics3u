# Documentation practice 2

def exclude(a: list, b: list) -> set:
    """
    Return the items in a that are not b.

    >>> exclude([1, 2, 3], [4, 5, 6])
    [1, 2, 3]
    >>> exclude([1, 2, 3], [1, 2, 3])
    []
    >>> exclude([1, 2, 3], [1, 2])
    [3]
    """

    only_in_a = []
    for item in a:
        if item not in b:
            only_in_a.append(item)
    return only_in_a
