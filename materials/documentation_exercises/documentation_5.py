# Documentation practice 5

"""
    TODO
        - Write a descriptive docstring that tells what it does
        - Give the function and all variables reasonable names
        - Write the type annotations
        - Write two docstring examples showing test cases
"""

def missed_ri(a):
    for i in range(1, a):
        print('x' * i)
    for i in range(1, a):
        print((' ' * (a - i)) + ('x' * i))
