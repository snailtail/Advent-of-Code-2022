import heapq
import re
from aoc import inpututil as iu
import os


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}
    
    def add_node(self, value):
        self.nodes.add(value)
        
    def add_edge(self, from_node, to_node, distance):
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance
        
    def dijkstra(self, start, end):
        # Initialize distances and previous nodes
        distances = {node: float('inf') for node in self.nodes}
        previous = {node: None for node in self.nodes}
        distances[start] = 0
        
        # Initialize priority queue
        queue = []
        heapq.heapify(queue)
        heapq.heappush(queue, (0, start))
        
        # Dijkstra's algorithm
        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_node == end:
                break


    def dijkstra_with_timer(self, graph, start, end, timer):
        # Initialize distances and previous nodes
        distances = {node: float('inf') for node in graph}
        previous = {node: None for node in graph}
        distances[start] = 0
        
        # Initialize priority queue
        queue = []
        heapq.heapify(queue)
        heapq.heappush(queue, (0, start))
        
        # Dijkstra's algorithm
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            
            if current_node == end:
                break
            
            for neighbor, weight in graph[current_node]:
                # Update weight based on remaining time
                weight *= timer
                
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))
                    
            # Deduct time
            timer -= 1
            
        # Construct shortest path
        path = []
        node = end
        while node is not None:
            path.insert(0, node)
            node = previous[node]
            
        return path, distances[end]


class VolcanoEvacuator:
    def __init__(self, input: list, timelimit: int=30) -> None:
        self.valves = set()
        self.timelimit=30
        #self.workload = deque()
        self.parseinput(input)

    def parseinput(self, lines: list):
        for line in lines:
            _valves = re.findall(r"([A-Z]{2})", line)
            _rate = int(re.findall(r"(rate=(\d))", line)[0][1])
            _id = _valves[0]
            _tunnels = [x for x in _valves[1:]]
            _thisvalve = Valve(id=_id, rate=_rate, tunnels=_tunnels)
            self.valves.add(_thisvalve)

        print(self.valves)
class Valve:
    def __init__(self, id: str, rate: int, tunnels: list) -> None:
        self.id = id
        self.rate = rate
        self.tunnels = tunnels

file=os.path.basename(__file__).replace('.py','')
util = iu()

lines = util.GetLines(file, test=True)

# Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
step1 = VolcanoEvacuator(input = lines, timelimit = 30)
