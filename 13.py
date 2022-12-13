from aoc import inpututil as iu
import os

file=os.path.basename(__file__).replace('.py','')
util = iu()


def compare(part1,part2):
    """
        Compare two parts of a pair.
        Returns -1 if part 1 is smaller than part 2.
        Returns 0 if they are equal
        Returns 1 if part 2 is smaller than part 1
    """
    if isinstance(part1, int) and isinstance(part2,int):
        # Both are integers
        if part1 < part2:
            return -1
        elif part1 == part2:
            return 0
        else:
            return 1
    elif isinstance(part1, list) and isinstance(part2, list):
        # Both are lists
        i = 0
        while i<len(part1) and i<len(part2):
            c = compare(part1[i], part2[i])
            if c==-1:
                return -1
            if c==1:
                return 1
            i += 1
        if i==len(part1) and i<len(part2):
            return -1
        elif i<len(part1) and i==len(part2):
            return 1
        else:
            return 0
    elif isinstance(part1, int) and isinstance(part2, list):
        # Part 1 is int, make it a list and run compare again
        return compare([part1], part2)
    else:
        # Part 2 is int, make it a list and run compare again
        return compare(part1, [part2])



def step1(input):
    result = 0
    for i, group in enumerate(input.strip().split('\n\n')):
        pair1, pair2 = group.split('\n')
        pair1 = eval(pair1)
        pair2 = eval(pair2)    
        if compare(pair1,pair2)==-1:
            result += i+1 # 1-based index...

    print(f"Step 1 {result}")



def main():
    data = util.GetContents(file, test=False)
    step1(data)

if __name__=="__main__":
    main()