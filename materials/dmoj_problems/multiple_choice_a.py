# Multiple Choice
# https://dmoj.ca/problem/ccc11s2

# Solution A

n = int(input())

student = ''
correct = ''
n_correct = 0

for i in range(n):
    student += input()

for i in range(n):
    correct += input()
    
for i in range(n):
    if student[i] == correct[i]:
        n_correct += 1

print(n_correct)
