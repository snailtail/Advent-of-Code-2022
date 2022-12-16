import re
from aoc import inpututil as iu
import os
from collections import deque

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

time=30
for line in lines:
    valves = re.findall(r"([A-Z]{2})", line)
    rate = int(re.findall(r"(rate=(\d))", line)[1])
    print(valves)
    print(rate)