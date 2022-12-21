from aoc import inpututil as iu
from collections import deque
import os

file=os.path.basename(__file__).replace('.py','')
util = iu()

iarr = util.GetIntArray(file, test=False, splitat='\n')

todo = deque(iarr)

while len(todo) > 0:
    movethis = todo.popleft()
    #print(f"{movethis} : {iarr}")
    index = iarr.index(movethis)
    newindex = abs((index + movethis) % (len(iarr)))
    
    #print(index, movethis, newindex)s
    if movethis != 0:
        iarr.insert(newindex, iarr.pop(index))
    #print(f"r:  {iarr}")

# find groove coordinates

zeroindex = iarr.index(0)
groove1 = iarr[(zeroindex + 1000) % (len(iarr))]
groove2 = iarr[(zeroindex + 2000) % (len(iarr))]
groove3 = iarr[(zeroindex + 3000) % (len(iarr))]

print(groove1+groove2+groove3)

