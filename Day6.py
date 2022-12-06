raw = open("inputs/6.txt","r").read().split()

for i in range(4,len(raw[0])):
    if len(set(raw[0][i:i+4])) == 4:
        print("Answer part 1: ",i+4)
        break

for i in range(14,len(raw[0])):
    if len(set(raw[0][i:i+14])) == 14:
        print("Answer part 1: ",i+14)
        break    
