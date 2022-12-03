import numpy as np

#raw = open("inputs/2t.txt","r").readlines()
raw = open("inputs/2.txt","r").readlines()
#input_array = [[int(item) for item in string.split('\n')] for string in raw.split('\n\n')[:]]

opPlays = ['A','B','C']
mePlays = ['X','Y','Z']
ans = 0
ans2 = 0

for round in raw:
    op, me = round.strip('\n').split(' ')
    ans += mePlays.index(me) + 1 
    if ((mePlays.index(me)-opPlays.index(op)) % 3) == 1:
        ans += 6
    elif ((mePlays.index(me)-opPlays.index(op)) % 3) == 0:
        ans += 3

print('Answer to part 1: ', ans)    

for round in raw:
    op, me = round.strip('\n').split(' ')
    if mePlays.index(me) == 0:
        ans2 += (opPlays.index(op) -1 ) % 3 + 1
    elif mePlays.index(me) == 1:
        ans2 += 3 + opPlays.index(op) + 1
    elif mePlays.index(me) == 2:
        ans2 += 6 + (opPlays.index(op) + 1 ) % 3 + 1

print('Answer to part 2: ', ans2)    
