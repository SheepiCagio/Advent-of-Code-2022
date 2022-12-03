#raw = open("inputs/3t.txt","r").read().split('\n')
raw = open("inputs/3.txt","r").read().split('\n')
#ASCII code a = 97, A = 65

ans=0
for backpack in raw:
    strings = [backpack[:(len(backpack)//2)], backpack[len(backpack)//2:]]
    common = list(set.intersection(*map(set,strings)))[0]
    if common.isupper():
        ans += ord(common)-38
    else:
        ans += ord(common)-96
print('Answer part 1: ', ans)    

ans2=0

for i in range(0,len(raw), 3):
    strings = []
    for x in range(0,3):
        strings.append(raw[i+x])
        strings.append(raw[i+x])
    common = list(set.intersection(*map(set,strings)))[0]
    if common.isupper():
        ans2 += ord(common)-38
    else:
        ans2 += ord(common)-96
print('Answer part 2: ', ans2)  
