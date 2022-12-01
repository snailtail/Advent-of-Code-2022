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

#sort the list in descending order
elfs.sort(reverse=True)

# Step 1 - The max calorie count for an elf
print(max(elfs))

# Step 2 - The sum of the max calorie count for the top three elfs.
print(sum(elfs[0:3]))