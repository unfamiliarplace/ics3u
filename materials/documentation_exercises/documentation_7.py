# Documentation practice 7

"""
    TODO
        - Write a descriptive docstring that tells what it does
        - Give the function and all variables reasonable names
        - Write the type annotations
        - Write two docstring examples showing test cases
"""

import random

def mistry(a):
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    if b == 1 and c == 1:
        return a * 2
    else:
        return a * -1
