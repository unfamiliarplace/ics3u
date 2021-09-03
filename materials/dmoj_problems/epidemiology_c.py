# Epidemiology
# https://dmoj.ca/problem/ccc20j2

# Contributed by Dr. Daniel Zingaro
# More elegant geometric series implementation -- no loop, runs instantly!

import math

P = int(input())
N = int(input())
R = int(input())

if N >= P:
     day = 1
elif R > 1:
     day = math.ceil(math.log((P + 1) * (R - 1)/N + 1, R) - 1)
elif R == 1:
     day = math.floor(P / N)

print(day)
