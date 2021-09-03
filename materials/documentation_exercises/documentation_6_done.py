# Documentation practice 6

"""
    TODO
        - Write a descriptive docstring that tells what it does
        - Give the function and all variables reasonable names
        - Write the type annotations
        - Write two docstring examples showing test cases
"""

def compare_words(first_word: str, second_word: str) -> int:
    """
    Compare first_word and second_word and return a sortable integer.
    Return -1 for the first being smaller, 0 for equal, 1 for first is larger.

    >>> compare_words('dog', 'cat')
    1
    >>> compare_words('cat', dog')
    -1
    >>> compare_words('cat', 'cat')
    0
    """
    if first_word.upper() < second_word.upper():
        return -1
    elif first_word.upper() > second_word.upper():
        return 1
    else:
        return 0
