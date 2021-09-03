# Multiple Choice
# https://dmoj.ca/problem/ccc11s2

# Solution B

n = int(input())

lines = ''
n_correct = 0

for i in range(n * 2):
    lines += input()
    
for i in range(n):
    if lines[i] == lines[n + i]:
        n_correct += 1

print(n_correct)
