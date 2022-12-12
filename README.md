# :christmas_tree: Advent of Code 2022 :christmas_tree:
[Advent of Code](https://adventofcode.com/2022) by [Eric Wastl](http://was.tl)

For this years challenge I will attempt to solve as many pussles as possible using Python 3 :snake:

- [- Day 1: Calorie Counting -](./01.md)  
Quite an easy start. Made a few touch-ups to the code after completing the challenge.

- [- Day 2: Rock Paper Scissors -](./02.md)
Not very complicated, I didn't have to keep track of player 1 - but as usual I'm trying to think ahead in step 1 what might come in step 2, so I made the basis around keeping track of both scores. Decided to leave it in - and step 2 was just a small routine in front of step 1.

- [- Day 3: Rucksack Reorganization -](./03.md)
A fun little exercise, searching for characters apperaring in multiple strings or parts of strings.

- [- Day 4: Camp Cleanup -](./04.md)
Today we had to check for overlap in ranges. Using sets in Python made things very easy, due to the intersect functionality.

- [- Day 5: Supply Stacks -](./05.md)
This one was a bit trickier, but after I discovered that Lists in Python could be handled almost like stacks it became easier. Spent way too much time on the parsing of the input. Tried regex for picking out the moves for the crane instead of splitting as I usually do.

- [- Day 6: Tuning Trouble -](./06.md)
Parsing a string looking for the first chunk consisting of unique characters. Using the set functionality to check for uniqueness.

- [- Day 7: No Space Left On Device - ](./07.md)
Tricky...!  Parsing "commands", building and storing the paths and calculating their sizes. Parsing the input was a bit on the tricky side today.

- [- Day 8: Treetop Tree House -](./08.md)
Basically just traversing a grid and counting values above a threshold. But oh my goodness how I struggled with off-by-one errors on this one...

- [- Day9: Day 9: Rope Bridge -](./09.md)
Keeping track of knots on a rope. For some reason this is one of those puzzles that seems quite easy, but I struggle immensely with... Painful to solve for some reason. Had to rewrite everything for step 2. >.<

- [- Day 10: Cathode-Ray Tube -](./10.md)
A lot of fun! Seems easier today than yesterday... At least for me.
Simulating a cathode ray tube, from a list of instructions.

- [- Day 11: Monkey in the Middle -](./11.md)
Holy mathematics Batman! Step 1 was mainly about getting on par with the parsing of the input. But step 2 was a nightmare which required research in the mathematical field, since I don't have an infinite amount of time, and/or five trillion petabytes of RAM. LCM to the rescue after some serious googling.
Overworked the solution a bit, with the Monkey class, but at least I didn't start out too "cheap" ending up having to rewrite everything for step 2 this time. :stuck_out_tongue_closed_eyes:

- [- Day 12: Hill Climbing Algorithm -](./12.md)
So I woke up to Graphs this morning, and wanted to go straight back to bed. But a bit of googling, and slowly remembering day 15 of last year I convinced myself to go ahead anyway. Last year I use Dijkstra's algorithm, but BFS seems to be a viable option - So let's implement Breadth First Search in Python then eh?