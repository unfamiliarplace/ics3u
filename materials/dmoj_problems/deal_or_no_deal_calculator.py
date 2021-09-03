# Deal or No Deal Calculator
# https://dmoj.ca/problem/ccc07j3

briefcases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

n_opened = int(input())
n_unopened = 10 - n_opened

for i in range(n_opened):
    briefcase = int(input())
    briefcases[briefcase - 1] = 0
    
offer = int(input())

average = sum(briefcases) / n_unopened

if offer > average:
    print('deal')
else:
    print('no deal')
