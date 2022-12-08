with open('day08/day08_input.txt','r') as f:
    grid=[[int(height) for height in str.strip(l)] for l in f.readlines()]

visible=0
for row in range(len(grid)):
        for col in range(len(grid[0])):
            treeheight = grid[row][col]
            if row == 0 or row == len(grid) - 1 or col == 0 or col == len(grid[0]) - 1:
                visible+=1
                continue

            # Top view
            for n in range(0, row):
                if grid[n][col] >= treeheight:
                    break
            else:
                visible+=1
                continue

            # Bottom view
            for n in range(row + 1, len(grid)):
                if grid[n][col] >= treeheight:
                    break
            else:
                visible+=1
                continue

            # Left view
            for n in range(0, col):
                if grid[row][n] >= treeheight:
                    break
            else:
                visible+=1
                continue

            # Right view
            for n in range(col + 1, len(grid[0])):
                if grid[row][n] >= treeheight:
                    break
            else:
                visible+=1
                continue

print(visible)