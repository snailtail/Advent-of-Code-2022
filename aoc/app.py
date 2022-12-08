import map

test = map.FourWayMap()
test.Move("Up 2")
print(test.coordinate())
print(test.CalculateManhattanDistance("3:-1"))