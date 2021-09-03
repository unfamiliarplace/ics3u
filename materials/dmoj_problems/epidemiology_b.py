# Epidemiology
# https://dmoj.ca/problem/ccc20j2

# Contributed by Alex Macri
# Faster loop solution (does not involve exponentiation)

P = int(input())
N = int(input())
R = int(input())

sick = N
n_days = 0

while sick <= P:
    n_days += 1
    N *= R # essentially stores the previous day's sick to avoid exponentiation
    sick += N

print(n_days)
