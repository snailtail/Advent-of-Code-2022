class CathodeRayTube():
    """
    A class representing a Cathode Ray Tube.

    This class has the following attributes:
    - cycles: An integer representing the current number of cycles the CRT has completed.
    - X: An integer representing the current X-coordinate of the CRT.
    - sum: An integer representing the current sum of signal strengths.
    - lines: A two-dimensional list of characters representing the current state of the CRT.

    This class has the following methods:
    - __init__: Initializes a new CRT with default values.
    - run: Executes a given instruction on the CRT.
    - noop: Does nothing for one cycle.
    - addV: Adds a given value to the X-coordinate of the CRT for two cycles.
    - check: Checks the current state of the CRT and updates its attributes accordingly.
    - drawsprite: Draws a sprite on the CRT at the current position of the X-coordinate.
    - displayPicture: Displays the current state of the CRT.
    """

    def __init__(self):
        self.cycles = 1
        self.X = 1
        self.sum = 0
        self.lines = [['.' for x in range(40)] for x in range(6)]

    def run(self, instruction):
        """
        Executes a given instruction on the CRT.

        This method takes in a list of strings representing the instruction to be executed on the CRT.
        The instruction can either be 'addx' or 'noop', followed by a value (if 'addx' is used).
        This method updates the attributes of the CRT accordingly.

        Example:
            tube = CathodeRayTube()
            tube.run(['addx', '10'])
        """
        self.check()
        if instruction[0] == 'addx':
            self.addV(int(instruction[1]))
        elif instruction[0] == 'noop':
            self.noop()

    def noop(self):
        """
        Does nothing for one cycle.

        This method increments the `cycles` attribute by 1 and calls the `check` method to update the state of the CRT.

        Example:
            tube = CathodeRayTube()
            tube.noop()
        """
        self.cycles += 1
        self.check()

    def addV(self, val):
        """
        Adds a given value to the X-coordinate of the CRT for two cycles.

        This method takes in an integer representing the value to be added to the X-coordinate of the CRT.
        This method increments the `cycles` attribute by 2, adds the given value to the `X` attribute,
        and calls the `check` method to update the state of the CRT.

        Example:
            tube = CathodeRayTube()
            tube.addV(10)
        """
        self.cycles += 1
        self.check()
        self.cycles += 1
        self.X += val
        self.check()

    def check(self):
        """
        Checks the current state of the CRT and updates its attributes accordingly.

        This method checks the current value of the `cycles` attribute and updates the `sum` and `lines` attributes
        of the CRT accordingly. If the value of `cycles` is in the range [20, 60, 100, 140, 180, 220], then the `sum` attribute
        is updated by adding the product of `cycles` and `X` to it. 
        Then a check is made to see which of the lines on the CRT to draw on, an then the `drawsprite` method is called to draw on that line.

        Example:
            tube = CathodeRayTube()
            tube.check()
        """
        if self.cycles in [20, 60, 100, 140, 180, 220]:
            signalstrength = self.cycles * self.X
            self.sum += signalstrength

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

        if self.cycles == 220:
            print(f"Step 1: {self.sum}")

    def drawsprite(self, line):
        """
        Draws the sprite on the line at the position of (cycles mod 40 -1), 
        if any part of the sprite is located at this pixel.
        """
        currpos = (self.cycles % 40) - 1
        if self.X == currpos or self.X - 1 == currpos or self.X + 1 == currpos:
            self.lines[line][currpos] = 'X'

    def displayPicture(self):
        for line in self.lines:
            print("".join(line))


with open('day10/day10_input.txt', 'r') as f:
    commands = [l.rstrip() for l in f.readlines()]

tube = CathodeRayTube()

for command in commands:
    command = command.split()
    tube.run(command)


tube.displayPicture()
