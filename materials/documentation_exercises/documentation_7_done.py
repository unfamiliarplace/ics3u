# Documentation practice 7

"""
    TODO
        - Write a descriptive docstring that tells what it does
        - Give the function and all variables reasonable names
        - Write the type annotations
        - Write two docstring examples showing test cases
"""

import random

def bet_snake_eyes(bet: int) -> int:
    """
    Roll 2 dice. If both are 1 (snake eyes), return double the bet.
    Otherwise return the negative of the bet.

    # Will not pass automatic testing, just to show what can happen
    >>> bet_snake_eyes(10)
    -10
    >>> bet_snake_eyes(10)
    20
    """
    
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    if die_1 == 1 and die_2 == 1:
        return bet * 2
    else:
        return bet * -1

