with open('day01/day01_input.txt') as f:
    lines = f.readlines()
    
elfs=[0,0]
index=1
for line in lines:
    if line.rstrip()=="":
       index+=1
       elfs.append(0)
    else:
        elfs[index]+= int(line.rstrip())
max=0
for elf in elfs:
    if elf > max:
        max=elf
print(max)
elfs.sort(reverse=True)
print(elfs[2]+elfs[1]+elfs[0])