from collections import defaultdict
import re

def extract_sizes(command):
    pattern = '\d+'
    sizes = [int(x) for x in re.findall(pattern, command)]
    return sizes

with open('day07/day07_input.txt', 'r') as file:
    lines = file.read()

dir_sizes = defaultdict(lambda : 0)
dir_tree = []

# Splitta på "$ cd" för att hitta alla actions som gör efter att man byter current workdir. Splitta sen detta på newlines, och leta fram alla numeriska värden som finns gömda i dessa.
for directory, size in [(command.split('\n')[0], sum(extract_sizes(command))) for command in lines.split('$ cd') if command != '']: 
    directory = directory.strip()
    if directory == '..':
        dir_tree.pop()
    else:
        dir_tree.append(directory)
    cur_dir = ''
    for sub_directory in dir_tree:
        cur_dir += (sub_directory + '/')
        dir_sizes[cur_dir] += size

# Step 1
# Summera alla som är under tröskeln
step1_sum=sum([size for directory, size in dir_sizes.items() if size < 100000])
print('Step 1: ', step1_sum)



# Step 2
# Hitta den minsta av de som är tillräckligt stora för att frigöra det önskade utrymmet
space_used = dir_sizes['//']
space_to_delete = 30000000 - (70000000 - space_used)
step2=min([size for directory, size in dir_sizes.items() if size >= space_to_delete])
print('Step 2: ', step2)