# Documentation practice 6

"""
    TODO
        - Write a descriptive docstring that tells what it does
        - Give the function and all variables reasonable names
        - Write the type annotations
        - Write two docstring examples showing test cases
"""

def mistaree(a, b):
    if a.upper() < b.upper():
        return -1
    elif a.upper() > b.upper():
        return 1
    else:
        return 0
