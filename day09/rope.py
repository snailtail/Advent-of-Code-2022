class PlanckRope():

    def __init__(self):
        pass
    
    def move(self, cur_position, direction):
        match direction.upper():
            case "R":
                return (cur_position[0] + 1, cur_position[1])
            case "L":
                return (cur_position[0] - 1, cur_position[1])
            case "U":
                return (cur_position[0], cur_position[1] + 1)
            case "D":
                return (cur_position[0], cur_position[1] - 1)
        

    def move_knot(self, knot, neighbor):
        knot_x, knot_y = knot
        neighbor_x, neighbor_y = neighbor
        new_tail = knot

        tail_needsmove = abs(knot_x - neighbor_x) > 1 or abs(knot_y - neighbor_y) > 1

        if not tail_needsmove:
            return knot

        if neighbor_x > knot_x:
            new_tail = self.move(new_tail, "R")
        elif neighbor_x < knot_x:
            new_tail = self.move(new_tail, "L")

        if neighbor_y > knot_y:
            new_tail = self.move(new_tail, "U")
        elif neighbor_y < knot_y:
            new_tail = self.move(new_tail, "D")

        return new_tail
        

    def count_visited_coordinates(self, moves, tail_length=1):
        start_coordinate = (0, 0)
        visited_coordinates = set([start_coordinate])

        head = start_coordinate
        tail = [start_coordinate] * tail_length

        for (direction, count) in moves:
            for _ in range(int(count)):
                head = self.move(head, direction)

                prev = head
                # for each knot in the rest of the body/tail, follow the nearest "previous knot"
                for i, knot in enumerate(tail):
                    tail[i] = self.move_knot(knot, prev)
                    prev = tail[i]

                visited_coordinates.add(tail[-1])

        return len(visited_coordinates)