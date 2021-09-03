# Uncrackable
# https://dmoj.ca/problem/wc17c3j3/resubmit/3608397

password = input()

# Flag to track whether it's valid. If anything makes it False, it stays False.
valid = True

# Counters for lowercase, uppercase, and digits
n_lower = 0
n_upper = 0
n_digit = 0

# Check length requirement
if len(password) < 8 or len(password) > 12:
    valid = False

# Tally characters
for char in password:
    if char.islower():
        n_lower += 1
    elif char.isupper():
        n_upper += 1
    elif char.isdigit():
        n_digit += 1
    else:
        valid = False

# Check the tallies
if (n_lower < 3) or (n_upper < 2) or (n_digit < 1):
    valid = False

# Print the output
if valid:
    print('Valid')
else:
    print('Invalid')
