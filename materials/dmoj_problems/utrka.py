# Utrka
# https://dmoj.ca/problem/coci14c2p2
# Attempt #2 with dictionaries

# The problem was that names weren't unique, so sets, which are unique, fail
# e.g. 3 jims and 2 bobs register. 2 jims and 2 bobs finish. jim is our man
# So we need to instead tally how many times we saw each name...

# 1. Count how many times each name appears in the list of registrants
#    and the list of people who finished
# 2. Find out which name occurs LESS in finished than in registered

n_registered = int(input())

# Set up empty dictionaries
people_registered = {}
people_finished = {}

# Read people who registered
for i in range(n_registered):
    name = input()

    # Tally how often we've seen each name
    if name not in people_registered:
        people_registered[name] = 1
    else:
        people_registered[name] += 1
    
    
# Read people who finished
for i in range(n_registered - 1):
    name = input()
    
    # Tally how often we've seen each name
    if name not in people_finished:
        people_finished[name] = 1
    else:
        people_finished[name] += 1

# Find the one person who didn't finish
for name in people_registered:
    if name not in people_finished:
        print(name)
    elif people_finished[name] < people_registered[name]:
        print(name)
