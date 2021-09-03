# Bard
# https://dmoj.ca/problem/crci06p1

n_vills = int(input())
n_evenings = int(input())

songs = []

for i in range(n_evenings):
    data = input().split()
    for j in range(len(data)):
        data[j] = int(data[j])
        
    n_attendees = data[0]
    attendees = set(data[1:])
    
    if 1 in attendees:
        songs.append(attendees)
        
    else:
        for attendee in attendees:
            for j in range(len(songs)):
                if attendee in songs[j]:
                    songs[j] = songs[j].union(attendees)

for i in range(n_vills):
    vill = i + 1
    in_all = True
    for knowers in songs:
        if vill not in knowers:
            in_all = False
    
    if in_all:
        print(vill)
