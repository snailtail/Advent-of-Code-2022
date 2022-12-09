from rope import PlanckRope

with open("day09/day09_input.txt",'r') as f:
    moves = [m.split() for m in f.readlines()]

rope = PlanckRope()
step1 = rope.count_visited_coordinates(moves)
print(f"Step 1: {step1}")