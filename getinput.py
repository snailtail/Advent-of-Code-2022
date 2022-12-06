import requests
import sys

if(len(sys.argv) > 1):
    daystring=sys.argv[1]
    day=int(sys.argv[1])
else:
    day=1
#print(day)

cookies={'session':'53616c7465645f5f5409cb374a934d5a30f344db4fd56b47e849e738f2463e581323b606db37bedc5fceffc8f47c9730e2824c89ff7d857feacf847a4cbcd836'}

r = requests.get(f"https://adventofcode.com/2022/day/{day}/input", cookies=cookies)
print(f"Downloading input for day{daystring}")
dayinput = r.content.decode().strip()
with (open(f"./day{daystring}/day{daystring}_input.txt",'w')) as f:
    f.write(dayinput)