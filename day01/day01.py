with open('day01/day01_input.txt') as f:
    lines = f.readlines()

# Create a list with some empty elfs - index 0 will not be used, and index 1 will start with 0 to be added upon
elfs=[0,0]
index=1
for line in lines:
    if line.rstrip()=="":
        # we hit a separator line - the next line will belong to a new elf
       index+=1
       elfs.append(0) # start out with a 0 value for the new elf
    else:
        elfs[index]+= int(line.rstrip())
max=0
for elf in elfs:
    if elf > max:
        max=elf

#sort the list in descending order, will make the max value appear in index 0
elfs.sort(reverse=True)
# Step 1 - The max calorie count for an elf
print(elfs[0])

# Step 2 - The sum of the max calorie count for the top three elfs.
print(elfs[2]+elfs[1]+elfs[0])