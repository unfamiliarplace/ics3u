# Epidemiology
# https://dmoj.ca/problem/ccc20j2

# Solution A

P = int(input())
N = int(input())
R = int(input())

sick = N
days = 0

while sick <= P:
    days += 1
    sick += (N * (R ** days))
    
print(days)
