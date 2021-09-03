# Documentation practice 3

"""
    TODO
        - Write a descriptive docstring that tells what it does
        - Give the function and all variables reasonable names
        - Write the type annotations
        - Write two docstring examples showing test cases
"""

def myst_ri(a):
    b = False
    c = False
    for d in a:
        if d.isupper():
            b = True
        elif d.islower():
            c = True
    return b and c
