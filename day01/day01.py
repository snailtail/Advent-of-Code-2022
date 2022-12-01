with open('day01/day01_input.txt', 'r') as f:
    lines = f.readlines()

# List will store the sums of each elfs calories
elfs=[]
calorie_sum=0
for line in lines:
    if line.rstrip()=="":
        # We hit a separator line - the next line will belong to a new elf
       elfs.append(calorie_sum) # Store this elfs total calories
       calorie_sum=0            # Reset for next elf
    else:
        calorie_sum+= int(line.rstrip()) # Just add to the current elfs total

# Sort the list in descending order
elfs.sort(reverse=True)

# Step 1 - The max calorie count for an elf
print(max(elfs))

# Step 2 - The sum of the max calorie count for the top three elfs.
print(sum(elfs[0:3]))