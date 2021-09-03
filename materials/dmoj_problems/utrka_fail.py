# Utrka
# https://dmoj.ca/problem/coci14c2p2
# Attempt #1 with sets

n_registered = int(input())

# Set up empty sets
people_registered = set()
people_finished = set()

# Read people who registered for the marathon
for i in range(n_registered):
    name = input()
    people_registered.add(name)
    
# Read people who finished the marathon
for i in range(n_registered - 1):
    name = input()
    people_finished.add(name)

# Find the one person who didn't finish
for person in people_registered:
    if person not in people_finished:
        print(person)
        break
