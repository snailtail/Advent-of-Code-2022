with open('day08/day08_testinput.txt','r') as f:
    treelines=[l.rstrip() for l in f.readlines()]

r=0
map={}
for line in treelines:
    for c in range(len(line)):
        coord=f"{r}:{c}"
        map[coord]=int(line[c])
    r+=1

print(map)