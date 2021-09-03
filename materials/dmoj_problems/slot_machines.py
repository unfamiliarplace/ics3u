# Slot Machines
# https://dmoj.ca/problem/ccc00s1

n_quarters = int(input())
A_plays = int(input())
B_plays = int(input())
C_plays = int(input())

n_plays = 0

on_machine = 'A'

while n_quarters > 0:
    n_plays += 1
    n_quarters -= 1
    
    if on_machine == 'A':
        A_plays += 1
        if A_plays == 35:
            n_quarters += 30
            A_plays = 0
        on_machine = 'B'

    elif on_machine == 'B':
        B_plays += 1
        if B_plays == 100:
            n_quarters += 60
            B_plays = 0
        on_machine = 'C'
        
    elif on_machine == 'C':
        C_plays += 1
        if C_plays == 10:
            n_quarters += 9
            C_plays = 0
        on_machine = 'A'

print(f'Martha plays {n_plays} times before going broke.')
