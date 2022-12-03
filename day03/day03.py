

def pairs(line):
    # Find the item type that appears in both compartments
    middle=int(len(line)/2)
    comp1=line[0:middle]
    comp2=line[middle:]
    for character in comp1:
        if character in comp2:
            return character
    
def getValue(n):
    # Get the value for each item type:
    if n.islower():
        return ord(n)-96
    else:
        return ord(n)-38
    


def main():
    data = [line.rstrip() for line in open('./day03/day03_input.txt','r')]
    step1_sum=0
    for item in data:
        step1_sum += getValue(pairs(item))
    print(step1_sum)

if __name__=="__main__":
    main()