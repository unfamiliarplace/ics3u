# Cezar
# https://dmoj.ca/problem/coci17c1p1

cards_drawn = []
cards_left = [
    2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
    8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
    10, 10, 10, 10, 11, 11, 11, 11]
    
# Draw cards based on input
n_drawn = int(input())
for i in range(n_drawn):
    
    # TODO Input the next card value
    # TODO Remove it from the list of cards left
    # TODO Add it to the list of cards drawn

# Find the difference to 21
sum_so_far = sum(cards_drawn)
diff_to_x = 21 - sum_so_far

n_greater = 0
# TODO Find the number of cards left whose value is > the difference to x

# Just subtract from total to count the other half
n_lesser = len(cards_left) - n_greater

# TODO Write the final print output ('DOSTA' for stop or 'VUCI' for draw)
