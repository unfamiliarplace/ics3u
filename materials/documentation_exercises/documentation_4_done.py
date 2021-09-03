# Documentation practice 4

def multiply_list(numbers: list) -> int:
    """
    Return the cumulative product of all the given numbers.

    >>> multiply_list([5, 7, 42])
    1470
    >>> multiply_list([5, 2, 0])
    0
    """
    
    product = 1
    for number in numbers:
        product *= number
    return product
