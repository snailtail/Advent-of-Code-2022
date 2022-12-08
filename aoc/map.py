import re
class FourWayMap():
        x = 0
        y = 0
        
        def coordinate(self):
            return f"{self.x}:{self.y}"
        
        visitedCoordinates = set()
        originCoordinate=""

        def __init__(self, X=0, Y=0):
            self.x = X
            self.y = Y;
            self.originCoordinate = self.coordinate()

        #region move_around

        def MoveUp(self, Steps):
            for i  in range(Steps):
                self.y+=1
                self.visitedCoordinates.add(self.coordinate())
        
        def MoveDown(self, Steps):
            for i  in range(Steps):
                self.y-=1
                self.visitedCoordinates.add(self.coordinate)

        def MoveRight(self, Steps):
            for i  in range(Steps):
                self.x+=1
                self.visitedCoordinates.add(self.coordinate)

        def MoveLeft(self, Steps):
            for i  in range(Steps):
                self.x-=1
                self.visitedCoordinates.add(self.coordinate)

        #endregion

        #region parse input
        def Move(self, MoveInstruction):
            

            direction = '?'
            steps = 0
            match = re.match(r"(\D+)(\d+)", MoveInstruction.lower())
            if match != None:
                direction = match[1].rstrip()
                steps = int(match[2])

            
            if direction in ["n","u","up","north"]:
                direction = "n"
            elif direction in ["s","d","down","south"]:
                direction = "s"
            elif direction in ["e","r","east","right"]:
                direction = "e"
            elif direction in ["w","l","west","left"]:
                direction = "w"
            
            self.DoMove(direction, steps)

        def DoMove(self, Direction, Steps):
            
                if Direction=="?":
                    print("Unknown Direction...!")
                elif Direction=="n":
                    self.MoveUp(Steps)
                elif Direction=="s":
                    self.MoveDown(Steps)
                elif Direction=="e":
                    self.MoveRight(Steps)
                elif Direction=="w":
                    self.MoveLeft(Steps)
                    
        def CalculateManhattanDistance(self, coord):
            coordData = coord.split(":")
            retX = abs(int(coordData[0]))
            retY = abs(int(coordData[1]))
            return retX + retY
        #end