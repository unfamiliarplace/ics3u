# Documentation practice 9

"""
    TODO
        - Write a descriptive docstring that tells what it does
        - Give the function and all variables reasonable names
        - Write the type annotations
        - Write two docstring examples showing test cases
"""

def miss_turry(a, b):
    c = {}
    a = a.lower()
    
    for d in a:
        if d not in c:
            c[d] = 1
        else:
            c[d] += 1

    e = []
    for f in c:
        if c[f] == b:
            e.append(f)

    return e
