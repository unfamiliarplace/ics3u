# Happy or Sad
# https://dmoj.ca/problem/ccc15j2

sentence = input()

n_happy = sentence.count(':-)')
n_sad = sentence.count(':-(')

if n_happy > n_sad:
    print('happy')
elif n_sad > n_happy:
    print('sad')
elif n_sad + n_happy == 0:
    print('none')
else:
    print('unsure')
