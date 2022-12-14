from collections import defaultdict
from aoc import inpututil as iu
import os

class Cavesystem:
    def __init__(self, rockpointdata: list) -> None:
        self.points=defaultdict(lambda: '.')
        for line in rockpointdata:
            # Get the different points for the paths of rock
            self.addpath(line.split(' -> '))
        self.getmaprange()

    
    def addpath(self, points: list):
        lastx, lasty = -1, -1
        for i, point in enumerate(points):
            px, py = map(int, point.split(','))
            if lastx == -1:
                lastx = px
            if lasty == -1:
                lasty = py
            for x in range(min(lastx,px), max(lastx,px) + 1):
                for y in range(min(lasty,py), max(lasty,py) + 1):
                    self.points[(x,y)] = '#'
            lastx = px
            lasty = py
    
    def addsand(self, startingpoint: tuple = (500,0)):
        x,y = startingpoint
        falling=True
        curpoint = startingpoint
        self.points[curpoint] = "+"
        while(falling):
            x,y = curpoint
            directions = {
                "s":(x,y+1),
                "sw":(x-1,y+1),
                "se":(x+1, y+1)
            }
            moved=False
            for dir in directions:
                if self.points[directions[dir]] == ".":
                    self.points[directions[dir]] = "+"
                    self.points[curpoint] = "."
                    curpoint=directions[dir]
                    #self.printmap()
                    #print("-"*10)
                    moved = True
                    break
                # no direction was possible to move in
            falling = moved
            x,y = curpoint
            
            # Check if we're outside the map area
            if x < self.minX or x > self.maxX or y > self.maxY:
                return False
        self.points[curpoint] = "o"
        #self.printmap()
        #print("-"*10)
        return True
            
    def printmap(self):
        for y in range(0, self.maxY+1):
            line=""
            for x in range(self.minX,self.maxX+1):
                p=(x,y)
                line += self.points[p]
            print(line)

    def getmaprange(self):
        coords = list(self.points.keys())
        minx = 10000000
        miny = 10000000
        maxx = 0
        maxy = 0
        for coord in coords:
            (x,y) = coord
            if x < minx:
                minx = x
            if x > maxx:
                maxx = x
            if y < miny:
                miny = y
            if y > maxy:
                maxy = y
        
        self.minX = minx
        self.minY = miny
        self.maxX = maxx
        self.maxY = maxy
            


file=os.path.basename(__file__).replace('.py','')
util = iu()



lines = util.GetLines(file, test=False)
cave = Cavesystem(lines)


#print(cave.points)
#cave.printmap()
#print("-"*10)
sandadded = 0
while(cave.addsand()):
    sandadded += 1    
print(sandadded)

