# Cezar
# https://dmoj.ca/problem/coci17c1p1

cards_drawn = []
cards_left = [
    2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
    8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
    10, 10, 10, 10, 11, 11, 11, 11]
    
# Draw cards based on input. Remove from cards left, add to cards drawn
n_drawn = int(input())
for i in range(n_drawn):
    card = int(input())
    cards_left.remove(card)
    cards_left.append(card)

# Find the difference to 21
diff_to_x = 21 - sum(cards_drawn)

# Find the number of cards left whose value is > the difference to x
n_greater = 0
for card in cards_left:
    if card > diff_to_x:
        n_greater += 1

# Just subtract from total to count the other half
n_lesser = len(cards_left) - n_greater

# Write the final print output ('DOSTA' for stop or 'VUCI' for draw)
if n_greater >= n_lesser:
    print('DOSTA')
else:
    print('VUCI')

