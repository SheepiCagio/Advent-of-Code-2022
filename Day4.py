import re

#raw = open("inputs/4t.txt","r").read().split('\n')
raw = open("inputs/4.txt","r").read().split('\n')

ans = 0 
for line in raw:
    (a,b,c,d) = [int(x) for x in re.split(r',|-',line)]
    if (c>=a and d<=b) or (a>=c and b<=d):
        ans += 1
        
print("Answer part 1: ",ans)

ans2 = 0 
for line in raw:
    (a,b,c,d) = [int(x) for x in re.split(r',|-',line)]
    if (c<=a<=d) or (c<=b<=d) or (a<=c<=b) or (a<=d<=b):
        ans2 += 1
print("Answer part 2: ", ans2)