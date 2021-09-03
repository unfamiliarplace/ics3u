# Documentation practice  1

"""
    TODO
        - Give the function and all variables reasonable names
        - Write the type annotations
        - Write a descriptive docstring that tells what it does
        - Write one docstring example showing a test case
"""

def mystery(a):
    
    b = []

    for c in a:
        if c % 2 == 0:
            b.append(c)

    return b
