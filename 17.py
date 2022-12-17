from collections import deque
from aoc import inpututil as iu
import os


# map is 7 units wide
# rock starts left edge 2 units away from left wall, and bottom three units above the highest rock
# (or the bottom if there are no rocks)
class Tetris:
    def __init__(self) -> None:
        self.highground = 0
        self.tetrismap = [['-','-','-','-','-','-','-'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.'],['.','.','.','.','.','.','.']]
        self.shapes = []
        self.moves = deque()

    def load_moves(self):
        data = util.GetContents(file, test=True)
        data = list(data)
        for move in data:
            self.moves.append(move)

    def append_empty_row(self):
        self.tetrismap.append(['.','.','.','.','.','.','.'])

    def play_shape(self, shapenum: int):
        # append top lines if needed
        shapenum = shapenum % 5
        shape = self.shapes[shapenum]
        while self.highground + (3 + len(shape)) > (len(self.tetrismap)-1):
            self.append_empty_row()
            
        #space_to_top_row = (len(self.tetrismap)-1) - (3 + len(shape))
        #space_to_add = self.highground - space_to_top_row
        #for n in range(space_to_add):
        #    self.append_empty_row()
        
        #draw the sprite
        topY=self.highground + len(shape) + 3 # remember where our top row of the sprite should be
        topX = 2
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                self.tetrismap[topY - row][col+topX] = shape[row][col]
        
        # now we need to move the shape first according to the move, and then down until it touches something
        while topY-len(shape) >= 0:
            if len(self.moves)==0:
                self.load_moves()
            move = self.moves.popleft()
            if move=='>':
                if self.can_move_right(shape,topY, topX):
                    self.move_right(shape,topY,topX)
                    topX += 1
            else:
                if self.can_move_left(shape,topY, topX):
                    self.move_left(shape,topY,topX)
                    topX -= 1
            #move 1 step down if possible
            if self.can_move_down(shape, topY, topX):
                self.move_down(shape, topY, topX)
                topY -=1
            else:
                self.highground=topY
                return False

    def move_down(self, shape: list, top_y: int, top_x: int):
        for col in range(len(shape[0])):
            #  för varje rad i shape - baklänges
            for row in range(len(shape)-1,-1,-1):
                if self.tetrismap[top_y-row][top_x+col] == '#':
                    self.tetrismap[top_y-row-1][top_x+col] = '#'
                    self.tetrismap[top_y-row][top_x+col] = '.'

    def can_move_down(self, shape: list, top_y: int, top_x: int):
        # för varje kolumn i shape:
        for col in range(len(shape[0])):
            #  för varje rad i shape - baklänges
            for row in range(len(shape)-1,-1,-1):
                # om vi slår i botten
                if top_y - row - 1 <=0:
                    return False
                elif shape[row][col] == '#':
                    if self.tetrismap[top_y - row - 1][top_x + col] == '#':
                        return False
                    else:
                        break
                else:
                    continue
        return True
                

    def move_left(self, shape: list, top_y: int, top_x):
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if self.tetrismap[top_y-row][top_x+col] == '#':
                    self.tetrismap[top_y-row][top_x+col-1] = '#'
                    self.tetrismap[top_y-row][top_x+col] = '.'

    def move_right(self, shape: list, top_y: int, top_x):
        for row in range(len(shape)):
            for col in range(len(shape[row])-1, -1, -1):
                if self.tetrismap[top_y-row][top_x+col] == '#':
                    self.tetrismap[top_y-row][top_x+col+1] = '#'
                    self.tetrismap[top_y-row][top_x+col] = '.'

    def can_move_left(self, shape: list, top_y: int, top_x):
        # check if anything o the left side of the shape blocks it from moving left
        canmove = True
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if top_x + col - 1 < 0:
                    #touches the left edge
                    return False
                elif shape[row][col]=='#': # this will determine the move for this row.
                    if self.tetrismap[top_y-row][top_x+col-1]=='#':
                        return False
                    else:
                        break
                else:
                    continue
        return True

    def can_move_right(self, shape: list, top_y: int, top_x):
        # check if anything o the right side of the shape blocks it from moving left
        canmove = True
        for row in range(len(shape)):
            for col in range(len(shape[row])-1,-1,-1):
                if len(self.tetrismap[0])-1 < top_x + col +1:
                    # touches the right edge
                    return False
                elif shape[row][col]=='#': # this will determine the move for this row.
                    if self.tetrismap[top_y-row][top_x+col+1]=='#':
                        return False
                    else:
                        break
                else:
                    continue
        return True

    def create_shapes(self):
        self.shapes.append([['#','#','#','#']])
        self.shapes.append([['.','#','.'],['#','#','#'],['.','#','.']])
        self.shapes.append([['.','.','#'],['.','.','#'],['#','#','#']])
        self.shapes.append([['#'],['#'],['#'],['#']])
        self.shapes.append([['#','#'],['#','#']])

    def print_shapes(self):
        for shape in self.shapes:
            for line in shape:
                print(''.join(line))
            print("")

    def print_map(self):
        for n in range(len(self.tetrismap)-1,-1,-1):
            print(''.join(self.tetrismap[n]), end="")
            print(f" {n}")

    def get_step1_result(self):    
        for row in range(len(self.tetrismap)-1, -1, -1):
            for cell in range(len(self.tetrismap[row])):
                if self.tetrismap[row][cell]=='#':
                    return row +1
                

file=os.path.basename(__file__).replace('.py','')
util = iu()


game = Tetris()
game.create_shapes()
game.print_map()
for n in range(0, 2023):
    game.play_shape(n)
    #game.print_map()

game.print_map()
print(game.get_step1_result())
print(game.highground)
