from rope import PlanckRope

with open('day09/day09_input.txt','r') as f:
    steps = [l.rstrip() for l in f.readlines()]

rope = PlanckRope(0,0)

for step in steps:
    rope.Move(step)

print(rope.tailPositions)
