# Documentation practice 9

"""
    TODO
        - Write a descriptive docstring that tells what it does
        - Give the function and all variables reasonable names
        - Write the type annotations
        - Write two docstring examples showing test cases
"""

def get_chars_occurring_n_times(s: str, n: int) -> list:
    """
    Return a list of the characters in s that occur exactly n times.

    >>> get_chars_occurring_n_times('tynan', 2)
    ['n']
    >>> get_chars_occurring_n_times('tynan', 1)
    ['t', 'y', 'a']
    """
    counts = {}
    s = s.lower()
    
    for char in s:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1

    result = []
    for char in counts:
        if counts[char] == n:
            result.append(f)

    return result
