import time
from aoc import inpututil as iu
import os
from collections import defaultdict
import re

class ExclusionZoneMap:
    
    def __init__(self, positiondata: list) -> None:
        self.zonemap = defaultdict(lambda: '.')
        self.minX, self.minY, self.maxX, self.maxY = 1000000, 1000000, 0, 0
        for line in positiondata:
            matches = re.findall(r"([x-y]=(-?\d+))",line)
            (xstring, sensorX),(ystring, sensorY),(bxstring,beaconX),(bystring,beaconY) = matches
            sensorX = int(sensorX)
            sensorY = int(sensorY)
            beaconX = int(beaconX)
            beaconY = int(beaconY)
            self.zonemap[(sensorX,sensorY)] = 'S'
            self.zonemap[(beaconX,beaconY)] = 'B'
            # check using manhattandistance for empty ('.') points in the map that are closer than the beacon, and mark them as #
            
            # for test
            #if sensorX == 8 and sensorY == 7
            self.markEmptyPoints(sensorX,sensorY,beaconX,beaconY)
            
            self.update_mincoords(min(sensorX,beaconX),min(sensorY,beaconY),max(sensorX,beaconX),max(sensorY,beaconY))
            #print(sensorX,sensorY,beaconX,beaconY)
    
    def getemptypoints(self,row):
        count=0
        for x in range(self.minX, self.maxX+1):
            if self.zonemap[(x,row)]=='#':
                count += 1
        return count
    
    def markEmptyPoints(self, sX, sY, bX, bY, importantrow=2000000):
        distance = self.getdistance(sX,sY,bX,bY)
        yrange = [importantrow] #range(sY-distance, sY+distance+1)
        xrange = range(sX-distance, sX+distance+1)
        for y in yrange:
            for x in xrange:
                if self.getdistance(sX,sY,x,y) <=distance:
                    if self.zonemap[(x,y)]=='.':
                        self.zonemap[(x,y)]='#'
                        self.update_mincoords(x,y,x,y)

    def getdistance(self, sx, sy, bx, by):
        return abs(sx-bx) + abs(sy-by)
    
    def update_mincoords(self, minX, minY, maxX, maxY):
        if minX < self.minX:
            self.minX = minX
        if minY < self.minY:
            self.minY = minY
        if maxX > self.maxX:
            self.maxX = maxX
        if maxY > self.maxY:
            self.maxY = maxY
            
    def printmap(self, step2=False):
        if step2:
            pass
        else:
            pass
        
        for y in range(self.minY, self.maxY+1):
            line=""
            for x in range(self.minX,self.maxX+1):
                p=(x,y)
                line += self.zonemap[p]
            print(line, y)
        time.sleep(0.1)

file=os.path.basename(__file__).replace('.py','')
util = iu()
lines = util.GetLines(file, test=False)
map = ExclusionZoneMap(lines)
#map.printmap()
print(map.getemptypoints(2000000))
print(map.minX,map.minY)



