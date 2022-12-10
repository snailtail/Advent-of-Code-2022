class CathodeRayTube():

    def __init__(self):
        self.cycles=1
        self.X=1
        self.sum=0
        self.lines=[['.' for x in range(40)] for x in range(6)]
    
    
    def run(self,instruction):
        self.check()
        if instruction[0]=='addx':
            self.addV(int(instruction[1]))
        elif instruction[0]=='noop':
            self.noop()
            
    def noop(self):
        self.cycles+=1
        self.check()


    def addV(self,val):
        self.cycles+=1
        self.check()
        self.cycles+=1
        self.X+=val
        self.check()

    def check(self):
        if self.cycles in [20, 60, 100, 140, 180, 220]:
            signalstrength = self.cycles * self.X
            self.sum+= signalstrength
            
        if -1 < self.cycles < 40:
            self.drawsprite(0)
        
        if 40 < self.cycles < 80:
            self.drawsprite(1)
        
        if 80 < self.cycles < 120:
            self.drawsprite(2)
        
        if 120 < self.cycles < 160:
            self.drawsprite(3)
            
        if 160 < self.cycles < 200:
            self.drawsprite(4)
        
        if 200 < self.cycles < 240:
            self.drawsprite(5)

        if self.cycles==220:
            print(f"Step 1: {self.sum}")

    def drawsprite(self,line):
        currpos = (self.cycles % 40) -1
        if self.X==currpos or self.X -1 ==currpos or self.X +1 == currpos:
            self.lines[line][currpos]='X'
            
    
    def displayPicture(self):
        for line in self.lines:
            print("".join(line))
                


with open('day10/day10_input.txt','r') as f:
    commands=[l.rstrip() for l in f.readlines()]

tube = CathodeRayTube()

for command in commands:
    command = command.split()
    tube.run(command)
    

tube.displayPicture()