# Trik
# https://dmoj.ca/problem/coci06c5p1

cup = 1

swaps = input()
for swap in swaps:
    
    if swap == 'A':
        if cup == 1:
            cup = 2
        elif cup == 2:
            cup = 1
    
    elif swap ==  'B':
        if cup == 2:
            cup = 3
        elif cup == 3:
            cup = 2
    
    elif swap == 'C':
        if cup == 1:
            cup = 3
        elif cup == 3:
            cup = 1

print(cup)
